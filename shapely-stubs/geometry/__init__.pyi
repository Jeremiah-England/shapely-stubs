"""
This type stub file was generated by pyright.
"""

import shapely.speedups

from .base import CAP_STYLE, JOIN_STYLE
from .collection import GeometryCollection
from .geo import asShape, box, mapping, shape
from .linestring import LineString, asLineString
from .multilinestring import MultiLineString, asMultiLineString
from .multipoint import MultiPoint, asMultiPoint
from .multipolygon import MultiPolygon, asMultiPolygon
from .point import Point, asPoint
from .polygon import LinearRing, Polygon, asLinearRing, asPolygon

"""Geometry classes and factories
"""
__all__ = [
    "box",
    "shape",
    "asShape",
    "Point",
    "asPoint",
    "LineString",
    "asLineString",
    "Polygon",
    "asPolygon",
    "MultiPoint",
    "asMultiPoint",
    "MultiLineString",
    "asMultiLineString",
    "MultiPolygon",
    "asMultiPolygon",
    "GeometryCollection",
    "mapping",
    "LinearRing",
    "asLinearRing",
    "CAP_STYLE",
    "JOIN_STYLE",
]
