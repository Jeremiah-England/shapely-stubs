from array import array
from collections.abc import Sequence
from typing import Any, Iterable, Literal, TypedDict

from shapely.coords import CoordinateSequence
from shapely.geometry import Polygon
from shapely.geometry.base import BaseGeometry
from shapely.geometry.proxy import CachingGeometryProxy

__all__ = ["Point", "asPoint"]

_PointInit = (
    Point
    | Iterable[float]
    | Iterable[tuple[float, float]]
    | Iterable[tuple[float, float, float]]
)

class _PointGeoJson(TypedDict):
    type: Literal["Point"]
    coordinates: tuple[float, float]

class _ArrayInterface(TypedDict):
    shape: tuple[Literal[0, 2, 3]]
    version: Literal[3]
    typestr: Literal["<f8", ">f8"]
    data: Any

class Point(BaseGeometry):
    def __init__(self, *args: _PointInit | float) -> None: ...
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    @property
    def z(self) -> float: ...
    @property
    def __geo_interface__(self) -> _PointGeoJson: ...
    def svg(
        self, scale_factor: float = ..., fill_color: str = ..., opacity: float = ...
    ) -> str: ...
    def array_interface(self) -> _ArrayInterface: ...
    @property
    def __array_interface__(self) -> _ArrayInterface: ...
    @property
    def bounds(self) -> tuple[()] | tuple[float, float, float, float]: ...
    coords: CoordinateSequence = ...
    @property
    def xy(self) -> tuple[array[float], array[float]]: ...
    def buffer(
        self,
        distance: float,
        resolution: int = ...,
        quadsegs: int = ...,
        cap_style: Literal[1, 2, 3] = ...,
        join_style: Literal[1, 2, 3] = ...,
        mitre_limit: float = ...,
        single_sided: bool = ...,
    ) -> Polygon: ...

class PointAdapter(CachingGeometryProxy, Point):
    _other_owned = ...
    def __init__(self, context: Sequence[float | tuple[float, float]]) -> None: ...
    @property
    def __array_interface__(self) -> _ArrayInterface: ...
    coords: CoordinateSequence = ...

def asPoint(context: Sequence[float | tuple[float, float]]) -> PointAdapter: ...
def geos_point_from_py(
    ob: _PointInit, update_geom: int = ..., update_ndim: Literal[0, 2, 3] = ...
) -> None | tuple[int, Literal[2, 3]]: ...
def update_point_from_py(geom: Point, ob: _PointInit): ...
