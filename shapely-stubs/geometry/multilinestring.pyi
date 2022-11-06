from collections.abc import Sequence
from typing import Literal, Optional, TypedDict

from shapely.geometry import LinearRing, LineString
from shapely.geometry.base import BaseMultipartGeometry
from shapely.geometry.proxy import CachingGeometryProxy

__all__ = ["MultiLineString", "asMultiLineString"]

_LineStringInit = LineString | LinearRing | Sequence[Sequence[float]]
_MultiLineStringInit = (
    MultiLineString | BaseMultipartGeometry | Sequence[_LineStringInit]
)

class _MultiLineStringGeoJson(TypedDict):
    type: Literal["MultiPoint"]
    coordinates: tuple[tuple[tuple[float, float], ...], ...] | tuple[
        tuple[tuple[float, float, float], ...], ...
    ]

class MultiLineString(BaseMultipartGeometry):
    def __init__(self, lines: Optional[_MultiLineStringInit] = ...) -> None: ...
    def shape_factory(self, *args) -> LineString: ...
    @property
    def __geo_interface__(self) -> _MultiLineStringGeoJson: ...
    def svg(
        self, scale_factor: float = ..., stroke_color: str = ..., opacity: float = ...
    ) -> str: ...

class MultiLineStringAdapter(CachingGeometryProxy, MultiLineString):
    context = ...
    _other_owned = ...
    def __init__(self, context: _MultiLineStringInit) -> None: ...

def asMultiLineString(context: _MultiLineStringInit) -> MultiLineStringAdapter: ...
def geos_multilinestring_from_py(
    ob: _MultiLineStringInit,
) -> tuple[int, Literal[2, 3]]: ...
