from collections.abc import Sequence
from typing import Literal, TypeAlias, TypedDict

from shapely.geometry import Point
from shapely.geometry.base import BaseMultipartGeometry
from shapely.geometry.proxy import CachingGeometryProxy

__all__ = ["MultiPoint", "asMultiPoint"]

_MultiPointInit: TypeAlias = MultiPoint | Sequence[Point | Sequence[float]]

class _MultiPointGeoJson(TypedDict):
    type: Literal["MultiPoint"]
    coordinates: tuple[tuple[float, float, float], ...] | tuple[
        tuple[float, float], ...
    ]

class _ArrayInterface(TypedDict):
    shape: tuple[int, Literal[2, 3]]
    version: Literal[3]
    typestr: Literal["<f8", ">f8"]
    data: Sequence[float]

class MultiPoint(BaseMultipartGeometry):
    def __init__(self, points: _MultiPointInit = ...) -> None: ...
    def shape_factory(self, *args) -> Point: ...
    @property
    def __geo_interface__(self) -> _MultiPointGeoJson: ...
    def svg(
        self, scale_factor: float = ..., fill_color: str = ..., opacity: float = ...
    ) -> str: ...
    @property
    def ctypes(self) -> Sequence[float]: ...
    def array_interface(self) -> _ArrayInterface: ...
    @property
    def __array_interface__(self) -> _ArrayInterface: ...

class MultiPointAdapter(CachingGeometryProxy, MultiPoint):
    context = ...
    _other_owned = ...
    def __init__(self, context: _MultiPointInit) -> None: ...
    @property
    def __array_interface__(self) -> _ArrayInterface: ...

def asMultiPoint(context: _MultiPointInit) -> MultiPointAdapter: ...
def geos_multipoint_from_py(ob: _MultiPointInit) -> tuple[int, Literal[2, 3]]: ...
