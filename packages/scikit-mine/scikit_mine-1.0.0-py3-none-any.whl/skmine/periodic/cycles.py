"""Periodic pattern mining with a MDL criterion"""
import copy
import json
import warnings
from datetime import timedelta, datetime

import numpy as np
import pandas as pd

from sklearn.utils.validation import check_is_fitted
from sklearn.base import BaseEstimator

from skmine.base import TransformerMixin
from .data_sequence import DataSequence
from .pattern import Pattern, getEDict, draw_pattern
from .pattern_collection import PatternCollection
from .run_mine import mine_seqs

# Authors: Rémi Adon <remi.adon@gmail.com>
#          Esther Galbrun <esther.galbrun@inria.fr>
#          Cyril Regan <cyril.regan@loria.fr>
#          Thomas Betton <thomas.betton@irisa.fr>
#          Hermann Courteille <hermann.courteille@irisa.fr>
#
# License: BSD 3 clause

INDEX_TYPES = (
    pd.DatetimeIndex,
    pd.RangeIndex,
    pd.Index,
)


class PeriodicPatternMiner(TransformerMixin, BaseEstimator):
    """
    Mining periodic cycles with a MDL Criterion

    PeriodicPatternMiner is an approach to mine periodic cycles from event logs
    while relying on a Minimum Description Length (MDL) criterion to evaluate
    candidate cycles. The goal here is to extract a set of cycles that characterizes
    the periodic structure present in the data

    A cycle is defined a 5-tuple of the form
        .. math:: \\alpha, r, p, \\tau, E

    Where

    - :math:`\\alpha` is the `repeating event`
    - :math:`r` is the number of repetitions of the event, called the `cycle length`
    - :math:`p` is the inter-occurrence distance, called the `cycle period`
    - :math:`\\tau` is the index of the first occurrence, called the `cycle starting point`
    - :math:`E` is a list of :math:`r - 1` signed integer offsets, i.e `cycle shift corrections`

    Parameters
    ----------

    complex: boolean
        True : compute complex pattern with horizontal and vertical combinations.
        False: compute only simple cycles.

    auto_time_scale: boolean
        True : preprocessing on time data index in nano-second. Compute automatically the timescale for mining cycles by removing
        extra zeros on time index and possibly change unit from second to upper ones
        False: no preprocessing on time data index in nano-second


    Examples
    --------
    >>> from skmine.periodic import PeriodicPatternMiner
    >>> import pandas as pd
    >>> S = pd.Series("ring_a_bell", [10, 20, 32, 40, 60, 79, 100, 240])
    >>> pcm = PeriodicPatternMiner().fit(S)
    >>> pcm.transform(S)
       t0                  pattern  repetition_major  period_major  sum_E
    0  20  (ring_a_bell)[r=5 p=20]                 5            20      2

    References
    ----------
    .. [1]
        Galbrun, E & Cellier, P & Tatti, N & Termier, A & Crémilleux, B
        "Mining Periodic Pattern with a MDL Criterion"
    """

    def __init__(self, complex=True, auto_time_scale=True):
        self.complex = complex
        self.auto_time_scale = auto_time_scale

    def _more_tags(self):
        return {
            "non_deterministic": True,
            "no_validation": True,
            "preserves_dtype": [],
            "requires_y": False,  # default for transformer
            "X_types": ['2darray']
        }

    def fit(self, S, y=None):
        """fit PeriodicPatternMiner on data logs

        This generates new candidate cycles and evaluate them.
        Residual occurrences are stored as an internal attribute,
        for later reconstruction (MDL is lossless)

        Parameters
        -------
        S: pd.Series
            logs, represented as a pandas Series
            This pandas Series must have an index of type in
            (pd.DatetimeIndex, pd.RangeIndex, pd.Int64Index)
        """

        self._validate_data(S, force_all_finite=False, accept_sparse=False, ensure_2d=False,
                            ensure_min_samples=2, dtype=str)

        if not isinstance(S, pd.Series):
            raise TypeError("S must be a pandas Series")

        if not isinstance(S.index, INDEX_TYPES):
            raise TypeError(f"S must have an index with a type amongst {INDEX_TYPES}")

        self.is_datetime_ = isinstance(S.index, pd.DatetimeIndex)
        serie = S.copy(deep=True)
        if serie.index.duplicated().any():  # there are potentially duplicates, i.e. occurrences that happened at the
            # same time AND with the same event. At this line, the second condition is not yet verified.
            len_S = len(serie)
            serie = serie.groupby(by=serie.index).apply(lambda x: x.drop_duplicates())
            # if same time and same event,  create Multi inde names =[timestamp, timestamp]
            diff = len_S - len(serie)
            if diff:
                serie = serie.reset_index(level=0, drop=True)
                warnings.warn(f"found {diff} duplicates in the input sequence, they have been removed.")

        S_times_nano = serie.index.astype("int64")
        verbose = False
        if self.auto_time_scale:
            converted_times_res, n_digit_nano_shifted, resolution, div_nb_sec = autoscale_time_unit(S_times_nano,
                                                                                                    verbose=False)
            serie.index = converted_times_res
            self.n_zeros_ = n_digit_nano_shifted
            self.div_nb_sec_ = div_nb_sec

        else:
            serie.index = S_times_nano
            resolution = "nano-second"
            self.div_nb_sec_ = 1

        self.resolution = resolution

        if verbose:
            print(f"Adjusted unit time for algorithm : {self.resolution}")

        self.alpha_groups_ = serie.groupby(serie.values).groups
        # associates to each event (key) its associated datetimes (list of values)
        cpool, data_details, pc = mine_seqs(dict(self.alpha_groups_), complex=self.complex)

        self.data_details_ = data_details
        self.miners_ = pc
        # self.cl, self.clRonly, self.clR, self.nb_simple, self.nbR, self.nbC = self.miners_.strDetailed(
        #     self.data_details_)
        return self

    def transform(self, S, dE_sum=True, chronological_order=True):
        """Return cycles as a pandas DataFrame, with 3 columns,
        with a 2-level multi-index: the first level mapping events,
        and the second level being positional

        Parameters
        -------
        dE_sum: boolean
            True : returm a columns "dE" with the sum of the errors
            False: returm a columns "dE" with the full list of errors.

        chronological_order: boolean, default=True
            To sort or not the occurences by ascending date

        Returns
        -------
        pd.DataFrame
            DataFrame with the following columns
                ==========  ======================================
                start       when the cycle starts
                length      number of occurrences in the event
                period      inter-occurrence delay
                sum_E       absolute sum of errors
                E           shift corrections (if dE_sum=False)
                cost        MDL cost
                ==========  ======================================

        Examples
        --------
        >>> from skmine.periodic import PeriodicPatternMiner
        >>> import pandas as pd
        >>> S = pd.Series("ring_a_bell", [10, 20, 32, 40, 60, 79, 100, 240])
        >>> pcm = PeriodicPatternMiner().fit(S)
        >>> pcm.transform(S)
           t0                  pattern  repetition_major  period_major  sum_E
        0  20  (ring_a_bell)[r=5 p=20]                 5            20      2
        """
        check_is_fitted(self, "miners_")
        global_stat_dict, patterns_list_of_dict = self.miners_.output_detailed(self.data_details_,
                                                                               n_zeros=self.n_zeros_,
                                                                               div_nb_sec=self.div_nb_sec_,
                                                                               is_datetime=self.is_datetime_)

        if not patterns_list_of_dict:
            return pd.DataFrame()  # FIXME

        self.cycles = pd.DataFrame(patterns_list_of_dict)

        if self.auto_time_scale:  # restore time in nano-second
            self.cycles.loc[:, ["t0", "period_major"]] *= (10 ** self.n_zeros_) * self.div_nb_sec_

            if self.is_datetime_:
                self.cycles.loc[:, "t0"] = self.cycles.t0.astype("datetime64[ns]")
                self.cycles.loc[:, "period_major"] = self.cycles.period_major.astype("timedelta64[ns]")
                self.cycles.loc[:, "E"] = self.cycles.E.map(np.array) * (10 ** self.n_zeros_ * self.div_nb_sec_)

                def to_timedelta(x): return pd.to_timedelta(x, unit='ns')

                self.cycles["E"] = self.cycles["E"].apply(lambda x: list(map(to_timedelta, x)))
        if dE_sum:
            self.cycles.rename(columns={"E": "sum_E"}, inplace=True)
            self.cycles["sum_E"] = self.cycles["sum_E"].apply(lambda x: np.sum(np.abs(x)))

        if chronological_order:
            self.cycles.sort_values(by='t0', inplace=True)

        dropped_col_for_output = ["pattern_json_tree"]

        return self.cycles.drop(columns=dropped_col_for_output, axis=1)

    def export_patterns(self, file="patterns.json"):
        """Export pattern into a json file

        Parameters
        -------
        file: string
            name of the json file
        """
        # allows us to call export_patterns without explicitly calling transform method before
        dummy_var = 17
        self.transform(dummy_var)

        big_dict_list = [i for i in self.cycles["pattern_json_tree"].values]

        data_dict = self.alpha_groups_.copy()
        for k, v in data_dict.items():
            data_dict[k] = v.to_list()

        big_dict = {
            "is_datetime_": self.is_datetime_,
            "n_zeros_": self.n_zeros_,
            "div_nb_sec_": self.div_nb_sec_,
            "data_details": data_dict,
            "patterns": big_dict_list
        }

        big_json_str = json.dumps(big_dict)
        with open(file, "w") as f:
            f.write(big_json_str)

    def import_patterns(self, file="patterns.json"):
        """Import pattern into a json file

        Parameters
        -------
        file: string
            name of the json file
        """

        with open(file, "r") as f:
            big_dict = json.load(f)

        self.n_zeros_ = big_dict["n_zeros_"]
        self.div_nb_sec_ = big_dict["div_nb_sec_"]
        self.is_datetime_ = big_dict["is_datetime_"]
        self.data_details_ = DataSequence(dict(big_dict["data_details"]))
        big_dict_list = big_dict["patterns"]

        patterns_list = []
        for pseudo_pat in big_dict_list:
            pattern = Pattern()
            pattern.next_id = pseudo_pat.pop("next_id")
            t0 = pseudo_pat.pop("t0")
            E = pseudo_pat.pop("E")
            pattern.nodes = _iterdict_str_to_int_keys(pseudo_pat)
            patterns_list.append((pattern, t0, E))

        patterns_collection = PatternCollection(patterns=patterns_list)
        self.miners_ = patterns_collection

    def reconstruct(self, *patterns_id, sort="time", drop_duplicates=None):
        """Reconstruct all the occurrences from patterns (no argument), or the
        occurrences of selected patterns (with a patterns'id list as argument).

        Parameters
        -------
        patterns_id: None or List
            None (when `reconstruct()` is called) : Reconstruct all occurrences of the patterns
            List : of pattern id : Reconstruct occurrences of the patterns ids

        sort: string
            "time" (by default) : sort by occurrences time
            "event" : sort by event names
            "construction_order" : sort by pattern reconstruction

        drop_duplicates: bool, default=True
            An occurrence can appear in several patterns and thus appear several times in the reconstruction.
            To remove duplicates, set drop_duplicates to True otherwise to False to keep them.
            In the natural order of pattern construction, it is best to set the `drop_duplicates` variable to False
            for better understanding.

        Returns
        -------
        pd.DataFrame
            The reconstructed dataset

        """
        if drop_duplicates is None:
            drop_duplicates = sort != "construction_order"

        reconstruct_list = []
        map_ev = self.data_details_.getNumToEv()

        if not patterns_id:
            patterns_id = range(len(self.miners_.getPatterns()))
        else:
            patterns_id = patterns_id[0]

        for pattern_id in patterns_id:
            (p, t0, E) = self.miners_.getPatterns()[pattern_id]

            occsStar = p.getOccsStar()
            Ed = getEDict(occsStar, E)
            occs = p.getOccs(occsStar, t0, Ed)

            for k, occ in enumerate(occs):
                if self.auto_time_scale:
                    time0 = occ * 10 ** self.n_zeros_ * self.div_nb_sec_ # restore time in nano-second
                else:
                    time0 = occ
                dict_ = {'time': time0,
                         "event": map_ev[occsStar[k][1]]}

                reconstruct_list.append(dict_)

        reconstruct_pd = pd.DataFrame(reconstruct_list)

        if self.is_datetime_:
            reconstruct_pd['time'] = reconstruct_pd['time'].astype("datetime64[ns]")
        else:
            reconstruct_pd['time'] = reconstruct_pd['time'].astype("int64")

        if sort == "time":
            reconstruct_pd = reconstruct_pd.sort_values(by=['time'])
        elif sort == "event":
            reconstruct_pd = reconstruct_pd.sort_values(by=['event'])

        # some events can be in multiple patterns : need to remove duplicates
        if drop_duplicates:
            reconstruct_pd = reconstruct_pd.drop_duplicates()

        return reconstruct_pd

    def get_residuals(self, *patterns_id, sort="time"):
        """Get all residual occurrences, i.e. events not covered by any pattern (no argument)
        or get the complementary occurrences of the selected patterns         (with a patterns'id list as argument).

        Parameters
        -------
        patterns_id: None or list
            None (when `reconstruct()` is called) : complementary of all patterns occurrences
            List of pattern id : complementary of patterns ids occurrences

        sort: string
            "time" (by default) : sort by occurrences time
            "event" : sort by event names
            anything else : sort by pattern reconstruction

        Returns
        -------
        pd.DataFrame
            residual events
        """

        if not patterns_id:
            patterns_id = range(len(self.miners_.getPatterns()))
        else:
            patterns_id = patterns_id[0]

        map_ev = self.data_details_.getNumToEv()
        residuals = self.miners_.getUncoveredOccs(self.data_details_)
        residuals_transf_list = []

        for res in residuals:
            if self.auto_time_scale:
                time0 = res[0] * 10 ** self.n_zeros_ * self.div_nb_sec_  # restore time in nano-second
            else:
                time0 = res[0]
            dict_ = {"time": time0, "event": map_ev[res[1]]}
            residuals_transf_list.append(dict_)

        residuals_transf_pd = pd.DataFrame(residuals_transf_list)

        if self.auto_time_scale and self.is_datetime_:
            residuals_transf_pd['time'] = residuals_transf_pd['time'].astype("datetime64[ns]")
        else:
            residuals_transf_pd['time'] = residuals_transf_pd['time'].astype("int64")

        reconstruct_ = self.reconstruct(patterns_id)
        reconstruct_all = self.reconstruct()
        complementary_reconstruct = reconstruct_all[~reconstruct_all.isin(reconstruct_)].dropna()

        if pd.merge(reconstruct_all, residuals_transf_pd, how='inner').empty:
            residuals_transf_pd = pd.concat([residuals_transf_pd, complementary_reconstruct], ignore_index=True)
        else:
            warnings.warn("residuals and complementary of reconstruct have common patterns")
            residuals_transf_pd = pd.concat([residuals_transf_pd, complementary_reconstruct], ignore_index=True)

        if sort == "time":
            residuals_transf_pd = residuals_transf_pd.sort_values(by=['time'])
        elif sort == "event":
            residuals_transf_pd = residuals_transf_pd.sort_values(by=['event'])

        return residuals_transf_pd

    def draw_pattern(self, pattern_id, directory=None):
        """
        Visually display a pattern based on its id from the transform command.

        Parameters
        ----------
        pattern_id : int
            The ID of the pattern to be displayed. This ID is to be retrieved directly from the transform command.

        directory : str, default=None
             Directory where the generated image and the DOT file are stored

        Returns
        -------
        Digraph
            The generated tree. To see it in a python script, you have to add .view()
        """
        # transform must have been called before draw_pattern
        if self.cycles is None:
            raise Exception("transform must have been called before draw_pattern")

        pattern = copy.deepcopy(self.cycles.loc[pattern_id]["pattern_json_tree"])
        # map each event id to its real textual name
        for nid in pattern.keys():
            if isinstance(nid, int):
                if "event" in pattern[nid].keys():
                    pattern[nid]["event"] = list(self.data_details_.map_ev_num.keys())[int(pattern[nid]["event"])]

                elif "p" in pattern[nid].keys():
                    if self.auto_time_scale:
                        pattern[nid]["p"] *= (10 ** self.n_zeros_ * self.div_nb_sec_)  # restore time in nano-second
                        if self.is_datetime_:
                            pattern[nid]["p"] = timedelta(microseconds=pattern[nid]["p"] / 1000)
                    for i, child in enumerate(pattern[nid]["children"]):
                        new_distance = child[1]
                        if i != 0 and self.auto_time_scale:
                            new_distance = child[1] * (
                                        10 ** self.n_zeros_ * self.div_nb_sec_)  # restore time in nano-second
                            if self.is_datetime_:
                                new_distance = timedelta(microseconds=new_distance / 1000)
                        pattern[nid]["children"][i] = (child[0], new_distance)

            elif nid == "t0":
                if self.auto_time_scale:
                    pattern["t0"] *= (10 ** self.n_zeros_ * self.div_nb_sec_)  # restore time in nano-second
                    if self.is_datetime_:
                        pattern["t0"] = datetime.utcfromtimestamp(pattern["t0"] / 1_000_000_000)

        graph = draw_pattern(pattern)
        if directory:
            graph.render(directory=directory)
        return graph


def autoscale_time_unit(S_times_nano, verbose=True):
    """ Convert times from nano-seconds to  upper unit , between ns and second, or in  {second, min, hour, day}

    Parameters
    ----------
    S_times_nano:  np.ndarray
      all timestamps in nano-second

    Returns
    -------
    converted_times : np.ndarray
        all times converted to one of the unit  {second, min, hour, day}
    n_digit_nano_shifted: int
        number of digit shifted from nano to eventually second
    resolution : str
        name of new unit time
    div_nb_sec : int
        number by which original times have been divided    { -    , 60, 3600, 24*3600}

    """
    shifted_times_in_nano, n_digit_nano_shifted = _shift_from_nano_to_sec(S_times_nano)
    if verbose:
        print(f"Auto_time_scale option: times in nano are divided by 10^{n_digit_nano_shifted}")

    if n_digit_nano_shifted < 9:
        converted_times = shifted_times_in_nano
        resolution = 'under_second'
        div_nb_sec = 1
    elif n_digit_nano_shifted == 9:
        converted_times, div_nb_sec, adjusted_resolution = shift_from_sec_to_upper_unit(shifted_times_in_nano)
        resolution = adjusted_resolution
        if verbose and div_nb_sec > 1:
            print(f"Auto_time_scale option: times in s are divided by {div_nb_sec} ")

    return converted_times, n_digit_nano_shifted, resolution, div_nb_sec


def shift_from_sec_to_upper_unit(original_times_in_sec: np.ndarray) -> tuple:
    """ Convert times in second to a un upper unit  {min, hour, day} , if no seconds are present in times ...

    Parameters
    ----------
    original_times_in_sec:  np.ndarray
      all timestamps in unit second
    """
    if (original_times_in_sec % 60 != 0).any():
        resolution = "second"
        div_nb = 1
    else:
        if (original_times_in_sec % (24 * 3600) == 0).all():
            resolution = 'day'
            div_nb = 24 * 3600
        elif (original_times_in_sec % 3600 == 0).all():
            resolution = "hour"
            div_nb = 3600
        elif (original_times_in_sec % 60 == 0).all():
            resolution = 'minute'
            div_nb = 60
    converted_times_res = original_times_in_sec // div_nb
    return converted_times_res, div_nb, resolution


def _shift_from_nano_to_sec(times_nano: np.ndarray) -> tuple:
    """ Drop all zeros on right side, common to all unix times in nano-second
    1s = 1_000_000_000 nano-second
     Parameters
    ----------
    times_nano:  np.ndarray
      all timestamps in nano-second
    """
    assert times_nano.dtype == np.int64

    n_unit_shifted = 0
    converted_times = np.copy(times_nano)
    second_digit_rank = 9
    while (converted_times % 10 == 0).all() and n_unit_shifted < second_digit_rank:
        converted_times //= 10
        n_unit_shifted += 1
    return converted_times, n_unit_shifted


def _iterdict_str_to_int_keys(dict_):
    """This function will recursively cast all string-keys to int-keys, if possible. If not possible the key-type
    will remain unchanged.
    """
    correctedDict = {}
    for key, value in dict_.items():
        if isinstance(value, list):
            value = [_iterdict_str_to_int_keys(item) if isinstance(item, dict) else item for item in value]
        elif isinstance(value, dict):
            value = _iterdict_str_to_int_keys(value)
        try:
            key = int(key)
        except Exception:
            pass
        correctedDict[key] = value

    return correctedDict

