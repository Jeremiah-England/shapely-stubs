from types import NotImplementedType
from typing import Any, Literal, overload

import numpy
import numpy.typing as npt
import shapely.errors

_C_API: PyCapsule
area: numpy.ufunc
boundary: numpy.ufunc
bounds: numpy.ufunc
box: numpy.ufunc
buffer: numpy.ufunc
build_area: numpy.ufunc
centroid: numpy.ufunc
clip_by_rect: numpy.ufunc
contains: numpy.ufunc
contains_properly: numpy.ufunc
convex_hull: numpy.ufunc
coverage_union: numpy.ufunc
covered_by: numpy.ufunc
covers: numpy.ufunc
create_collection: numpy.ufunc
crosses: numpy.ufunc
delaunay_triangles: numpy.ufunc
destroy_prepared: numpy.ufunc
difference: numpy.ufunc
difference_prec: numpy.ufunc
disjoint: numpy.ufunc
distance: numpy.ufunc
dwithin: numpy.ufunc
envelope: numpy.ufunc
equals: numpy.ufunc
equals_exact: numpy.ufunc
extract_unique_points: numpy.ufunc
force_2d: numpy.ufunc
force_3d: numpy.ufunc
frechet_distance: numpy.ufunc
frechet_distance_densify: numpy.ufunc
from_geojson: numpy.ufunc
from_wkb: numpy.ufunc
from_wkt: numpy.ufunc
geos_capi_version: tuple[int, int, int]
geos_capi_version_string: str
geos_version: tuple[int, int, int]
geos_version_string: str
get_coordinate_dimension: numpy.ufunc
get_dimensions: numpy.ufunc
get_exterior_ring: numpy.ufunc
get_geometry: numpy.ufunc
get_interior_ring: numpy.ufunc
get_num_coordinates: numpy.ufunc
get_num_geometries: numpy.ufunc
get_num_interior_rings: numpy.ufunc
get_num_points: numpy.ufunc
get_point: numpy.ufunc
get_precision: numpy.ufunc
get_srid: numpy.ufunc
get_type_id: numpy.ufunc
get_x: numpy.ufunc
get_y: numpy.ufunc
get_z: numpy.ufunc
has_z: numpy.ufunc
hausdorff_distance: numpy.ufunc
hausdorff_distance_densify: numpy.ufunc
intersection: numpy.ufunc
intersection_all: numpy.ufunc
intersection_prec: numpy.ufunc
intersects: numpy.ufunc
is_ccw: numpy.ufunc
is_closed: numpy.ufunc
is_empty: numpy.ufunc
is_geometry: numpy.ufunc
is_missing: numpy.ufunc
is_prepared: numpy.ufunc
is_ring: numpy.ufunc
is_simple: numpy.ufunc
is_valid: numpy.ufunc
is_valid_input: numpy.ufunc
is_valid_reason: numpy.ufunc
length: numpy.ufunc
line_interpolate_point: numpy.ufunc
line_interpolate_point_normalized: numpy.ufunc
line_locate_point: numpy.ufunc
line_locate_point_normalized: numpy.ufunc
line_merge: numpy.ufunc
linearrings: numpy.ufunc
linestrings: numpy.ufunc
make_valid: numpy.ufunc
minimum_bounding_circle: numpy.ufunc
minimum_bounding_radius: numpy.ufunc
minimum_clearance: numpy.ufunc
normalize: numpy.ufunc
offset_curve: numpy.ufunc
oriented_envelope: numpy.ufunc
overlaps: numpy.ufunc
point_on_surface: numpy.ufunc
points: numpy.ufunc
polygonize: numpy.ufunc
polygonize_full: numpy.ufunc
polygons: numpy.ufunc
prepare: numpy.ufunc
registry: list[type]
"""A list of geometry classes (e.g. LineString, Point, GeometryCollection, etc)."""
relate: numpy.ufunc
relate_pattern: numpy.ufunc
remove_repeated_points: numpy.ufunc
reverse: numpy.ufunc
segmentize: numpy.ufunc
set_precision: numpy.ufunc
set_srid: numpy.ufunc
shared_paths: numpy.ufunc
shortest_line: numpy.ufunc
simplify: numpy.ufunc
simplify_preserve_topology: numpy.ufunc
snap: numpy.ufunc
symmetric_difference: numpy.ufunc
symmetric_difference_all: numpy.ufunc
symmetric_difference_prec: numpy.ufunc
to_geojson: numpy.ufunc
to_wkb: numpy.ufunc
to_wkt: numpy.ufunc
touches: numpy.ufunc
unary_union: numpy.ufunc
unary_union_prec: numpy.ufunc
union: numpy.ufunc
union_prec: numpy.ufunc
voronoi_polygons: numpy.ufunc
within: numpy.ufunc

class ShapelyError(Exception): ...
class GEOSException(ShapelyError): ...

class Geometry:
    _geom: int
    _geom_prepared: int
    def __eq__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> NotImplementedType: ...
    def __gt__(self, other: Any) -> NotImplementedType: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: Any) -> NotImplementedType: ...
    def __lt__(self, other: Any) -> NotImplementedType: ...
    def __ne__(self, other: Any) -> bool: ...

class STRtree:
    _ptr: int
    count: int
    @classmethod
    def __init__(cls, geometries: npt.NDArray[Any], node_capacity: int, /) -> None: ...
    def dwithin(
        self, geometries: npt.NDArray[Any], distance: npt.NDArray[numpy.float64], /
    ) -> npt.NDArray[numpy.int64]: ...
    def nearest(self, geometries: npt.NDArray[Any]) -> npt.NDArray[numpy.int64]: ...
    def query(
        self, geometries: npt.NDArray[Any], predicate: int, /
    ) -> npt.NDArray[numpy.int64]: ...
    def query_nearest(
        self,
        geometry: npt.NDArray[Any],
        max_distance: float,
        exclusive: bool,
        all_matches: bool,
        /,
    ) -> tuple[npt.NDArray[numpy.int64], npt.NDArray[numpy.float64]]: ...

def _setup_signal_checks(interval: int, thread_id: int, /) -> None: ...
def count_coordinates(geometries: npt.NDArray[numpy.object_], /) -> int: ...
@overload
def get_coordinates(
    geometries: npt.NDArray[numpy.object_],
    include_z: bool,
    return_index: Literal[True],
    /,
) -> tuple[npt.NDArray[numpy.float64], npt.NDArray[numpy.int64]]: ...
@overload
def get_coordinates(
    geometries: npt.NDArray[numpy.object_],
    include_z: bool,
    return_index: Literal[False],
    /,
) -> npt.NDArray[numpy.float64]: ...
@overload
def get_coordinates(
    geometries: npt.NDArray[numpy.object_], include_z: bool, return_index: bool, /
) -> npt.NDArray[numpy.float64] | tuple[
    npt.NDArray[numpy.float64], npt.NDArray[numpy.int64]
]: ...
def get_coordinates(
    geometries: npt.NDArray[numpy.object_], include_z: bool, return_index: bool, /
) -> npt.NDArray[numpy.float64] | tuple[
    npt.NDArray[numpy.float64], npt.NDArray[numpy.int64]
]: ...
def set_coordinates(
    geometries: npt.NDArray[numpy.object_], coordinates: npt.NDArray[numpy.float64], /
) -> npt.NDArray[numpy.object_]:
    """Set the coordinates for an array of geometries inplace, returning the original array."""
    ...
