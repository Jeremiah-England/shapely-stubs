from collections.abc import Callable
from typing import Protocol

from shapely.coords import CoordinateSequence

class _HasCoords(Protocol):
    coords: CoordinateSequence

def signed_area(ring: _HasCoords) -> float: ...
def is_ccw_impl(name) -> Callable[[_HasCoords], bool]: ...
