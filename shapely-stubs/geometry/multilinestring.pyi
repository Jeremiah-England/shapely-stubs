"""
This type stub file was generated by pyright.
"""

from shapely.geometry.base import BaseMultipartGeometry
from shapely.geometry.proxy import CachingGeometryProxy

"""Collections of linestrings and related utilities
"""
__all__ = ["MultiLineString", "asMultiLineString"]

class MultiLineString(BaseMultipartGeometry):
    """
    A collection of one or more line strings

    A MultiLineString has non-zero length and zero area.

    Attributes
    ----------
    geoms : sequence
        A sequence of LineStrings
    """

    def __init__(self, lines=...) -> None:
        """
        Parameters
        ----------
        lines : sequence
            A sequence of line-like coordinate sequences or objects that
            provide the numpy array interface, including instances of
            LineString.

        Example
        -------
        Construct a collection containing one line string.

          >>> lines = MultiLineString( [[[0.0, 0.0], [1.0, 2.0]]] )
        """
        ...
    def shape_factory(self, *args): ...
    @property
    def __geo_interface__(self): ...
    def svg(
        self, scale_factor=..., stroke_color=..., opacity=...
    ):  # -> LiteralString | Literal['<g />']:
        """Returns a group of SVG polyline elements for the LineString geometry.

        Parameters
        ==========
        scale_factor : float
            Multiplication factor for the SVG stroke-width.  Default is 1.
        stroke_color : str, optional
            Hex string for stroke color. Default is to use "#66cc99" if
            geometry is valid, and "#ff3333" if invalid.
        opacity : float
            Float number between 0 and 1 for color opacity. Default value is 0.8
        """
        ...

class MultiLineStringAdapter(CachingGeometryProxy, MultiLineString):
    context = ...
    _other_owned = ...
    def __init__(self, context) -> None: ...

def asMultiLineString(context):  # -> MultiLineStringAdapter:
    """Adapts a sequence of objects to the MultiLineString interface"""
    ...

def geos_multilinestring_from_py(ob): ...