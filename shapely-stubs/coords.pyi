"""
This type stub file was generated by pyright.
"""

from shapely.topology import Validating

"""Coordinate sequence utilities
"""

class CoordinateSequence:
    """
    Iterative access to coordinate tuples from the parent geometry's coordinate
    sequence.

    Example:

      >>> from shapely.wkt import loads
      >>> g = loads('POINT (0.0 0.0)')
      >>> list(g.coords)
      [(0.0, 0.0)]

    """

    _cseq = ...
    _ndim = ...
    __p__ = ...
    def __init__(self, parent) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    @property
    def ctypes(self): ...
    def array_interface(self):  # -> dict[str, Unknown]:
        """Provide the Numpy array protocol."""
        ...
    __array_interface__ = ...
    @property
    def xy(self):  # -> tuple[array[float], array[float]]:
        """X and Y arrays"""
        ...

class BoundsOp(Validating):
    def __init__(self, *args) -> None: ...
    def __call__(self, this): ...
