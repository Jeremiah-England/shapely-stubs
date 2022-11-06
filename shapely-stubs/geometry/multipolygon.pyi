from collections.abc import Iterable, Sequence
from typing import Literal, Optional, TypedDict, overload

from shapely.geometry.base import BaseMultipartGeometry
from shapely.geometry.polygon import Polygon
from shapely.geometry.proxy import CachingGeometryProxy

__all__ = ["MultiPolygon", "asMultiPolygon"]

_MultiPolygonInitGeoJson = Sequence[Sequence[Sequence[Sequence[float]]]]
_MultiPolygonInitPoly = (
    MultiPolygon
    | BaseMultipartGeometry
    | Iterable[Polygon | Sequence[Sequence[Sequence[float]]]]
)

class _MultiPolygonGeoJson(TypedDict):
    type: "MultiPolygon"
    coordinates: list[tuple[tuple[tuple[float, float], ...], ...]] | list[
        tuple[tuple[tuple[float, float, float], ...], ...]
    ]

class MultiPolygon(BaseMultipartGeometry):
    @overload
    def __init__(
        self,
        polygons: _MultiPolygonInitPoly = ...,
        context_type: Literal["polygons"] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        polygons: _MultiPolygonInitGeoJson = ...,
        context_type: Literal["geojson"] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self, polygons: None = ..., context_type: Literal["polygons", "geojson"] = ...
    ) -> None: ...
    def __init__(
        self,
        polygons: Optional[_MultiPolygonInitPoly | _MultiPolygonInitGeoJson] = ...,
        context_type: Literal["polygons", "geojson"] = ...,
    ) -> None: ...
    def shape_factory(self, *args) -> Polygon: ...
    @property
    def __geo_interface__(self) -> _MultiPolygonInitGeoJson: ...
    def svg(
        self, scale_factor: float = ..., fill_color: str = ..., opacity: float = ...
    ) -> str: ...

class MultiPolygonAdapter(CachingGeometryProxy, MultiPolygon):
    context = ...
    _other_owned = ...
    def __init__(
        self, context, context_type: Literal["polygons", "geojson"] = ...
    ) -> None: ...

def asMultiPolygon(context) -> MultiPolygonAdapter: ...
def geos_multipolygon_from_py(
    ob: _MultiPolygonInitGeoJson,
) -> tuple[int, Literal[2, 3]]: ...
def geos_multipolygon_from_polygons(
    arg: _MultiPolygonInitPoly,
) -> tuple[int, Literal[2, 3]]: ...
