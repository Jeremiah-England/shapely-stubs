from logging import Logger
from typing import (
    Any,
    Callable,
    Generator,
    Iterator,
    Literal,
    NoReturn,
    Optional,
    overload,
)

from shapely.geometry import (
    GeometryCollection,
    LinearRing,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from shapely.impl import GEOSImpl, delegated

log: Logger = ...

_GeometryTypeStrs = Literal[
    "Point",
    "LineString",
    "LinearRing",
    "Polygon",
    "MultiPoint",
    "MultiLineString",
    "MultiPolygon",
    "GeometryCollection",
]

_Dimensions = Literal[2, 3]

GEOMETRY_TYPES: list[_GeometryTypeStrs] = ...

_Coord2 = tuple[float, float]
_Coord3 = tuple[float, float, float]
_Coords2 = list[_Coord2]
_Coords3 = list[_Coords3]
_Coords2WithHoles = list[_Coord2 | _Coords2]
_Coords3WithHoles = list[_Coord3 | _Coords3]
_Polygon2Coords = _Coords2 | _Coords2WithHoles
_Polygon3Coords = _Coords3 | _Coords3WithHoles
_AllBaseCoords = _Coord2 | _Coord3 | _Polygon2Coords | _Polygon3Coords

@overload
def dump_coords(geom: Point | LineString | LinearRing) -> _Coords2 | _Coords3: ...
@overload
def dump_coords(geom: Polygon) -> _Polygon2Coords | _Polygon3Coords: ...
@overload
def dump_coords(
    geom: MultiPoint | MultiLineString,
) -> list[_Coords2] | list[_Coords3]: ...
@overload
def dump_coords(
    geom: MultiPolygon,
) -> list[_Polygon2Coords] | list[_Polygon3Coords]: ...
@overload
def dump_coords(
    geom: GeometryCollection,
) -> list[_AllBaseCoords | list[_AllBaseCoords]]: ...
def dump_coords(
    geom: BaseGeometry,
) -> list[_AllBaseCoords | list[_AllBaseCoords]] | _AllBaseCoords: ...
def geometry_type_name(g: int) -> _GeometryTypeStrs: ...
def geom_factory(
    g: int, parent: Optional[BaseMultipartGeometry] = ...
) -> BaseGeometry: ...
def deserialize_wkb(data: bytes) -> int: ...
def geos_geom_from_py(
    ob: BaseGeometry, create_func: Optional[Callable[[Any], BaseGeometry]] = ...
) -> tuple[int, _Dimensions]: ...
def exceptNull(func): ...

class CAP_STYLE:
    round: Literal[1] = ...
    flat: Literal[2] = ...
    square: Literal[3] = ...

class JOIN_STYLE:
    round: Literal[1] = ...
    mitre: Literal[2] = ...
    bevel: Literal[3] = ...

EMPTY: int = ...

class BaseGeometry:
    __geom__: int = ...
    __p__: Optional[BaseGeometry] = ...
    _ctypes_data = ...
    _ndim: Optional[_Dimensions] = ...
    _crs = ...
    _other_owned: bool = ...
    _is_empty: bool = ...
    impl: GEOSImpl = ...
    _lgeos = ...
    def empty(self, val: Optional[int] = ...): ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __del__(self): ...
    def __str__(self) -> str: ...
    def __reduce__(self) -> tuple[type, tuple, bytes]: ...
    def __setstate__(self, state: bytes): ...
    def __setattr__(self, name: str, value: Any): ...
    def __and__(self, other: BaseGeometry) -> BaseGeometry: ...
    def __or__(self, other: BaseGeometry) -> BaseGeometry: ...
    def __sub__(self, other: BaseGeometry) -> BaseGeometry: ...
    def __xor__(self, other: BaseGeometry) -> BaseGeometry: ...
    def __eq__(self, other: BaseGeometry) -> bool: ...
    def __ne__(self, other: BaseGeometry) -> bool: ...

    __hash__: None = ...
    @property
    def ctypes(self) -> NoReturn: ...
    @property
    def array_interface_base(self) -> NoReturn: ...
    @property
    def __array_interface__(self) -> NoReturn: ...
    coords: NoReturn = ...
    @property
    def xy(self) -> NoReturn: ...
    @property
    def __geo_interface__(self) -> NoReturn: ...
    def geometryType(self) -> _GeometryTypeStrs: ...
    @property
    def type(self) -> _GeometryTypeStrs: ...
    @property
    def wkt(self) -> str: ...
    @property
    def wkb(self) -> bytes: ...
    @property
    def wkb_hex(self) -> str: ...
    def svg(self, scale_factor: int = ..., **kwargs) -> NoReturn: ...
    @property
    def geom_type(self) -> _GeometryTypeStrs: ...
    @property
    def area(self) -> float: ...
    def distance(self, other: BaseGeometry) -> float: ...
    def hausdorff_distance(self, other: BaseGeometry) -> float: ...
    @property
    def length(self) -> float: ...
    @property
    def minimum_clearance(self) -> float: ...
    @property
    def boundary(self) -> BaseGeometry: ...
    @property
    def bounds(self) -> tuple[()] | tuple[float, float, float, float]: ...
    @property
    def centroid(self) -> Point: ...
    @delegated
    def representative_point(self) -> Point: ...
    @property
    def convex_hull(self) -> BaseGeometry: ...
    @property
    def envelope(self) -> Point | Polygon: ...
    @property
    def minimum_rotated_rectangle(self) -> BaseGeometry: ...
    def buffer(
        self,
        distance: float,
        resolution: int = ...,
        quadsegs: int = ...,
        cap_style: Literal[1, 2, 3] = ...,
        join_style: Literal[1, 2, 3] = ...,
        mitre_limit: float = ...,
        single_sided: bool = ...,
    ) -> Polygon | MultiPolygon: ...
    @delegated
    def simplify(self, tolerance, preserve_topology=...) -> BaseGeometry: ...
    def normalize(self) -> BaseGeometry: ...
    def difference(self, other: BaseGeometry) -> BaseGeometry: ...
    def intersection(self, other: BaseGeometry) -> BaseGeometry: ...
    def symmetric_difference(self, other: BaseGeometry) -> BaseGeometry: ...
    def union(self, other: BaseGeometry) -> BaseGeometry: ...
    @property
    def has_z(self) -> bool: ...
    @property
    def is_empty(self) -> bool: ...
    @property
    def is_ring(self) -> bool: ...
    @property
    def is_closed(self) -> bool: ...
    @property
    def is_simple(self) -> bool: ...
    @property
    def is_valid(self) -> bool: ...
    def relate(self, other: BaseGeometry) -> str: ...
    def covers(self, other: BaseGeometry) -> bool: ...
    def covered_by(self, other: BaseGeometry) -> bool: ...
    def contains(self, other: BaseGeometry) -> bool: ...
    def crosses(self, other: BaseGeometry) -> bool: ...
    def disjoint(self, other: BaseGeometry) -> bool: ...
    def equals(self, other: BaseGeometry) -> bool: ...
    def intersects(self, other: BaseGeometry) -> bool: ...
    def overlaps(self, other: BaseGeometry) -> bool: ...
    def touches(self, other: BaseGeometry) -> bool: ...
    def within(self, other: BaseGeometry) -> bool: ...
    def equals_exact(self, other: BaseGeometry, tolerance: float) -> bool: ...
    def almost_equals(self, other: BaseGeometry, decimal: int = ...) -> bool: ...
    def relate_pattern(self, other: BaseGeometry, pattern: str) -> bool: ...
    @delegated
    def project(self, other: Point, normalized: bool = ...): ...
    @delegated
    @exceptNull
    def interpolate(self, distance: float, normalized: bool = ...) -> Point: ...

class BaseMultipartGeometry(BaseGeometry):
    def shape_factory(self, *args) -> NoReturn: ...
    @property
    def ctypes(self) -> NoReturn: ...
    @property
    def __array_interface__(self) -> NoReturn: ...
    @property
    def coords(self) -> NoReturn: ...
    @property
    def geoms(self) -> GeometrySequence | list[BaseGeometry]: ...
    def __bool__(self) -> bool: ...
    def __iter__(self) -> Iterator[BaseGeometry]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index) -> BaseGeometry: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...

    __hash__: None = ...
    def svg(self, scale_factor: int = ..., color: Optional[str] = ...) -> str: ...

class GeometrySequence:
    shape_factory: None = ...
    _geom: None = ...
    __p__: None = ...
    _ndim: None = ...
    def __init__(
        self, parent: BaseMultipartGeometry, type: Callable[..., BaseGeometry]
    ) -> None: ...
    def __iter__(self) -> Generator[BaseGeometry, None, None]: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, key: int) -> BaseGeometry: ...
    @overload
    def __getitem__(self, key: slice) -> BaseMultipartGeometry: ...
    def __getitem__(self, key: int | slice) -> BaseGeometry: ...

class HeterogeneousGeometrySequence(GeometrySequence):
    def __init__(self, parent: GeometryCollection) -> None: ...

class EmptyGeometry(BaseGeometry):
    def __init__(self) -> None: ...
