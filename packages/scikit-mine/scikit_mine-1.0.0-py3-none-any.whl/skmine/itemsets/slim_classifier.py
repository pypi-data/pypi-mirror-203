import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_is_fitted

from ..itemsets.slim import SLIM


class SlimClassifier(BaseEstimator, ClassifierMixin):
    """
    Classifier using the SLIM compression algorithm. Works for binary and multi-class problems.

    This classifier uses one SLIM instance per class in the database, resulting in a code table per class.
    To classify a transaction, we simply assign the class belonging to the code table that provides the minimal encoded
    length for the transaction.

    Parameters
    ----------
    items: set, default=None
        The list of items in the complete dataset not only the training set. This improves the accuracy of the model.
        Without this set of items, the classifier works but is less good in particular with small datasets.

    pruning: bool, default=False
        Indicates whether each SLIM classifier enables pruning

    Attributes
    ----------
    classes_ : array-like
        All the unique classes

    models_ : list
        A list of SLIM instances corresponding to *classes_*

    classes_X_ : list
        A list where each element is a subset of X and each element contains the transactions of X associated
        with the class from *classes_*  of the same index
    """

    def __init__(self, items=None, pruning=False):
        self.items = items
        self.pruning = pruning

    def _more_tags(self):
        return {"non_deterministic": True,
                "no_validation": True,
                "preserves_dtype": []}

    def fit(self, X, y):
        """Fit the model according to the given training data.

        Parameters
        ----------
        X: iterable, {array_like}
            containing n_transactions containing themselves n_items

        y: array-like of shape (n_samples,)
            Target vector relative to X.

        Returns
        -------
        self : object
            An instance of the estimator
        """
        self._validate_data(X, y, reset=True, validate_separately=False, force_all_finite=False,
                            accept_sparse=False, ensure_2d=False, ensure_min_samples=0, dtype=list)
        self.classes_ = np.unique(y)
        self.classes_X_ = []
        self.models_ = []

        for c in self.classes_:
            transactions_classes = [transaction for transaction, target in zip(X, y) if target == c]
            self.classes_X_.append(transactions_classes)
            self.models_.append(SLIM(items=self.items))

        for model, data in zip(self.models_, self.classes_X_):
            model.fit(data)

        return self

    def predict(self, X):
        """Perform classification on samples in X

        Parameters
        ----------
        X : iterable containing n_transactions containing themselves n_items

        Returns
        -------
        y_pred : np.array of shape (n_samples,)
            Class labels for samples in X
        """
        check_is_fitted(self, "classes_")
        self.models_scores = np.vstack([model.decision_function(X).values for model in self.models_]).T

        return self.classes_[self.models_scores.argmax(axis=1)]

    def __copy__(self):
        return SlimClassifier(items=self.items, pruning=self.pruning)
