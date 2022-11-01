"""
This type stub file was generated by pyright.
"""

import warnings
from functools import wraps

import shapely.affinity
from shapely import coords
from shapely.geometry import linestring, polygon

def method_wrapper(f): ...

__all__ = ["available", "enable", "disable", "enabled"]
_orig = ...
enabled = ...

def enable():  # -> None:
    """Enable Cython speedups

    The shapely.speedups module contains performance enhancements written in C.
    They are automatically installed when Python has access to a compiler and
    GEOS development headers during installation, and are enabled by default.

    You can check if speedups are installed with the `available` attribute, and
    check if they have been enabled with the `enabled` attribute.

    >>> from shapely import speedups
    >>> speedups.available
    True
    >>> speedups.enable()
    >>> speedups.enabled
    True
    """
    ...

def disable():  # -> None:
    """Disable Cython speedups"""
    ...

if available: ...