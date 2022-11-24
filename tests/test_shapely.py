"""Tests for types of objects defined in shapely's __init__.py file."""
from shapely import __version__
from typing_extensions import assert_type


def test_version():
    assert isinstance(assert_type(__version__, str), str)
