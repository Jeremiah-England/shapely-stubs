from array import array
from typing import Any, Iterable, Literal, Sequence, TypedDict

from shapely.coords import CoordinateSequence
from shapely.geometry import LinearRing, MultiLineString, Point
from shapely.geometry.base import BaseGeometry
from shapely.geometry.proxy import CachingGeometryProxy

__all__ = ["LineString", "asLineString"]

class _LineStringGeoJson(TypedDict):
    type: Literal["LineString"]
    coordinates: tuple[tuple[float, float], ...] | tuple[
        tuple[float, float, float], ...
    ]

class _ArrayInterface(TypedDict):
    shape: tuple[int, Literal[2, 3]]
    version: Literal[3]
    typestr: Literal["<f8", ">f8"]
    data: Any

_LineStringInit = LineString | LinearRing | Iterable[Sequence[float] | Point]

class LineString(BaseGeometry):
    def __init__(self, coordinates: _LineStringInit = ...) -> None: ...
    @property
    def __geo_interface__(self) -> _LineStringGeoJson: ...
    def svg(
        self, scale_factor: float = ..., stroke_color: str = ..., opacity: float = ...
    ) -> str: ...
    def array_interface(self) -> _ArrayInterface: ...
    @property
    def __array_interface__(self) -> _ArrayInterface: ...

    coords: CoordinateSequence = ...
    @property
    def xy(self) -> tuple[array[float], array[float]]: ...
    def parallel_offset(
        self,
        distance: float,
        side: Literal["left", "right"] = ...,
        resolution: int = ...,
        join_style: Literal[1, 2, 3] = ...,
        mitre_limit: float = ...,
    ) -> LineString | MultiLineString: ...

class LineStringAdapter(CachingGeometryProxy, LineString):
    def __init__(self, context: Sequence[Sequence[float]]) -> None: ...
    @property
    def __array_interface__(self) -> _ArrayInterface: ...
    coords: CoordinateSequence = ...

def asLineString(context: Sequence[Sequence[float]]) -> LineStringAdapter: ...
def geos_linestring_from_py(
    ob: _LineStringInit, update_geom: int = ..., update_ndim: Literal[2, 3] = ...
): ...
def update_linestring_from_py(geom: LineString, ob: _LineStringInit): ...
