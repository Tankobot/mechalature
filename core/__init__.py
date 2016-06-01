"""Mechalature core package."""

from core.reader import *
from core.identify import *

__all__ = [
    # reader vars
    'Reader',
    'ReaderError',
    'ReaderValueError',

    # identify vars
    'MechalatureEvent',
    'get_info',

    # package vars
    'MechalatureError',
]


class MechalatureError(Exception):
    pass
