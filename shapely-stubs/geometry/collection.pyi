from typing import Literal, Optional, Sequence, TypeAlias, TypedDict

from shapely.geometry.base import (
    BaseGeometry,
    BaseMultipartGeometry,
    HeterogeneousGeometrySequence,
)

_GeometryCollectionInit: TypeAlias = BaseMultipartGeometry | Sequence[BaseGeometry]

class _GeoJsonGeometry(TypedDict):
    type: str
    coordinates: tuple

class _GeometryCollectionGeoJson(TypedDict):
    type: Literal["GeometryCollection"]
    geometries: list[_GeoJsonGeometry]

class GeometryCollection(BaseMultipartGeometry):
    def __init__(self, geoms: Optional[_GeometryCollectionInit] = ...) -> None: ...
    @property
    def __geo_interface__(self) -> _GeometryCollectionGeoJson: ...
    @property
    def geoms(self) -> HeterogeneousGeometrySequence | list[BaseGeometry]: ...

def geos_geometrycollection_from_py(
    ob: _GeometryCollectionInit,
) -> tuple[int, Literal[2, 3]]: ...
