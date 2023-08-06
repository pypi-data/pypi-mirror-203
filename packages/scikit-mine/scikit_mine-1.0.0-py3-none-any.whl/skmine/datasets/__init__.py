"""
The :mod:`skmine.datasets` module includes utilities to load datasets,
including methods to load and fetch popular reference datasets.
"""
from ._base import get_data_home
from ._samples_generator import make_classification, make_transactions
from .periodic import fetch_canadian_tv, fetch_health_app, fetch_ubiq
