"""Tests for the shapely.lib module."""
import threading
from types import NotImplementedType

import numpy
import numpy.typing as npt
import pytest
from shapely.geometry.linestring import LineString
from shapely.geometry.point import Point
from shapely.lib import (
    _setup_signal_checks,  # pyright: ignore (importing private function)
)
from shapely.lib import (
    Geometry,
    GEOSException,
    ShapelyError,
    STRtree,
    area,
    boundary,
    bounds,
    box,
    buffer,
    build_area,
    centroid,
    clip_by_rect,
    contains,
    contains_properly,
    convex_hull,
    count_coordinates,
    coverage_union,
    covered_by,
    covers,
    create_collection,
    crosses,
    delaunay_triangles,
    destroy_prepared,
    difference,
    difference_prec,
    disjoint,
    distance,
    dwithin,
    envelope,
    equals,
    equals_exact,
    extract_unique_points,
    force_2d,
    force_3d,
    frechet_distance,
    frechet_distance_densify,
    from_geojson,
    from_wkb,
    from_wkt,
    geos_capi_version,
    geos_capi_version_string,
    geos_version,
    geos_version_string,
    get_coordinate_dimension,
    get_coordinates,
    get_dimensions,
    get_exterior_ring,
    get_geometry,
    get_interior_ring,
    get_num_coordinates,
    get_num_geometries,
    get_num_interior_rings,
    get_num_points,
    get_point,
    get_precision,
    get_srid,
    get_type_id,
    get_x,
    get_y,
    get_z,
    has_z,
    hausdorff_distance,
    hausdorff_distance_densify,
    intersection,
    intersection_all,
    intersection_prec,
    intersects,
    is_ccw,
    is_closed,
    is_empty,
    is_geometry,
    is_missing,
    is_prepared,
    is_ring,
    is_simple,
    is_valid,
    is_valid_input,
    is_valid_reason,
    length,
    line_interpolate_point,
    line_interpolate_point_normalized,
    line_locate_point,
    line_locate_point_normalized,
    line_merge,
    linearrings,
    linestrings,
    make_valid,
    minimum_bounding_circle,
    minimum_bounding_radius,
    minimum_clearance,
    normalize,
    offset_curve,
    oriented_envelope,
    overlaps,
    point_on_surface,
    points,
    polygonize,
    polygonize_full,
    polygons,
    prepare,
    registry,
    relate,
    relate_pattern,
    remove_repeated_points,
    reverse,
    segmentize,
    set_coordinates,
    set_precision,
    set_srid,
    shared_paths,
    shortest_line,
    simplify,
    simplify_preserve_topology,
    snap,
    symmetric_difference,
    symmetric_difference_all,
    symmetric_difference_prec,
    to_geojson,
    to_wkb,
    to_wkt,
    touches,
    unary_union,
    unary_union_prec,
    union,
    union_prec,
    voronoi_polygons,
    within,
)
from typing_extensions import assert_type


def test_area():
    assert isinstance(assert_type(area, numpy.ufunc), numpy.ufunc)


def test_boundary():
    assert isinstance(assert_type(boundary, numpy.ufunc), numpy.ufunc)


def test_bounds():
    assert isinstance(assert_type(bounds, numpy.ufunc), numpy.ufunc)


def test_box():
    assert isinstance(assert_type(box, numpy.ufunc), numpy.ufunc)


def test_buffer():
    assert isinstance(assert_type(buffer, numpy.ufunc), numpy.ufunc)


def test_build_area():
    assert isinstance(assert_type(build_area, numpy.ufunc), numpy.ufunc)


def test_centroid():
    assert isinstance(assert_type(centroid, numpy.ufunc), numpy.ufunc)


def test_clip_by_rect():
    assert isinstance(assert_type(clip_by_rect, numpy.ufunc), numpy.ufunc)


def test_contains():
    assert isinstance(assert_type(contains, numpy.ufunc), numpy.ufunc)


def test_contains_properly():
    assert isinstance(assert_type(contains_properly, numpy.ufunc), numpy.ufunc)


def test_convex_hull():
    assert isinstance(assert_type(convex_hull, numpy.ufunc), numpy.ufunc)


def test_coverage_union():
    assert isinstance(assert_type(coverage_union, numpy.ufunc), numpy.ufunc)


def test_covered_by():
    assert isinstance(assert_type(covered_by, numpy.ufunc), numpy.ufunc)


def test_covers():
    assert isinstance(assert_type(covers, numpy.ufunc), numpy.ufunc)


def test_create_collection():
    assert isinstance(assert_type(create_collection, numpy.ufunc), numpy.ufunc)


def test_crosses():
    assert isinstance(assert_type(crosses, numpy.ufunc), numpy.ufunc)


def test_delaunay_triangles():
    assert isinstance(assert_type(delaunay_triangles, numpy.ufunc), numpy.ufunc)


def test_destroy_prepared():
    assert isinstance(assert_type(destroy_prepared, numpy.ufunc), numpy.ufunc)


def test_difference():
    assert isinstance(assert_type(difference, numpy.ufunc), numpy.ufunc)


def test_difference_prec():
    assert isinstance(assert_type(difference_prec, numpy.ufunc), numpy.ufunc)


def test_disjoint():
    assert isinstance(assert_type(disjoint, numpy.ufunc), numpy.ufunc)


def test_distance():
    assert isinstance(assert_type(distance, numpy.ufunc), numpy.ufunc)


def test_dwithin():
    assert isinstance(assert_type(dwithin, numpy.ufunc), numpy.ufunc)


def test_envelope():
    assert isinstance(assert_type(envelope, numpy.ufunc), numpy.ufunc)


def test_equals():
    assert isinstance(assert_type(equals, numpy.ufunc), numpy.ufunc)


def test_equals_exact():
    assert isinstance(assert_type(equals_exact, numpy.ufunc), numpy.ufunc)


def test_extract_unique_points():
    assert isinstance(assert_type(extract_unique_points, numpy.ufunc), numpy.ufunc)


def test_force_2d():
    assert isinstance(assert_type(force_2d, numpy.ufunc), numpy.ufunc)


def test_force_3d():
    assert isinstance(assert_type(force_3d, numpy.ufunc), numpy.ufunc)


def test_frechet_distance():
    assert isinstance(assert_type(frechet_distance, numpy.ufunc), numpy.ufunc)


def test_frechet_distance_densify():
    assert isinstance(assert_type(frechet_distance_densify, numpy.ufunc), numpy.ufunc)


def test_from_geojson():
    assert isinstance(assert_type(from_geojson, numpy.ufunc), numpy.ufunc)


def test_from_wkb():
    assert isinstance(assert_type(from_wkb, numpy.ufunc), numpy.ufunc)


def test_from_wkt():
    assert isinstance(assert_type(from_wkt, numpy.ufunc), numpy.ufunc)


def test_geos_capi_version():
    assert isinstance(assert_type(geos_capi_version, tuple[int, int, int]), tuple)
    assert len(geos_capi_version) == 3
    assert all(isinstance(x, int) for x in geos_capi_version)


def test_geos_capi_version_string():
    assert isinstance(assert_type(geos_capi_version_string, str), str)


def test_geos_version():
    assert isinstance(assert_type(geos_version, tuple[int, int, int]), tuple)
    assert len(geos_version) == 3
    assert all(isinstance(x, int) for x in geos_version)


def test_geos_version_string():
    assert isinstance(assert_type(geos_version_string, str), str)


def test_get_coordinate_dimension():
    assert isinstance(assert_type(get_coordinate_dimension, numpy.ufunc), numpy.ufunc)


def test_get_dimensions():
    assert isinstance(assert_type(get_dimensions, numpy.ufunc), numpy.ufunc)


def test_get_exterior_ring():
    assert isinstance(assert_type(get_exterior_ring, numpy.ufunc), numpy.ufunc)


def test_get_geometry():
    assert isinstance(assert_type(get_geometry, numpy.ufunc), numpy.ufunc)


def test_get_interior_ring():
    assert isinstance(assert_type(get_interior_ring, numpy.ufunc), numpy.ufunc)


def test_get_num_coordinates():
    assert isinstance(assert_type(get_num_coordinates, numpy.ufunc), numpy.ufunc)


def test_get_num_geometries():
    assert isinstance(assert_type(get_num_geometries, numpy.ufunc), numpy.ufunc)


def test_get_num_interior_rings():
    assert isinstance(assert_type(get_num_interior_rings, numpy.ufunc), numpy.ufunc)


def test_get_num_points():
    assert isinstance(assert_type(get_num_points, numpy.ufunc), numpy.ufunc)


def test_get_point():
    assert isinstance(assert_type(get_point, numpy.ufunc), numpy.ufunc)


def test_get_precision():
    assert isinstance(assert_type(get_precision, numpy.ufunc), numpy.ufunc)


def test_get_srid():
    assert isinstance(assert_type(get_srid, numpy.ufunc), numpy.ufunc)


def test_get_type_id():
    assert isinstance(assert_type(get_type_id, numpy.ufunc), numpy.ufunc)


def test_get_x():
    assert isinstance(assert_type(get_x, numpy.ufunc), numpy.ufunc)


def test_get_y():
    assert isinstance(assert_type(get_y, numpy.ufunc), numpy.ufunc)


def test_get_z():
    assert isinstance(assert_type(get_z, numpy.ufunc), numpy.ufunc)


def test_has_z():
    assert isinstance(assert_type(has_z, numpy.ufunc), numpy.ufunc)


def test_hausdorff_distance():
    assert isinstance(assert_type(hausdorff_distance, numpy.ufunc), numpy.ufunc)


def test_hausdorff_distance_densify():
    assert isinstance(assert_type(hausdorff_distance_densify, numpy.ufunc), numpy.ufunc)


def test_intersection():
    assert isinstance(assert_type(intersection, numpy.ufunc), numpy.ufunc)


def test_intersection_all():
    assert isinstance(assert_type(intersection_all, numpy.ufunc), numpy.ufunc)


def test_intersection_prec():
    assert isinstance(assert_type(intersection_prec, numpy.ufunc), numpy.ufunc)


def test_intersects():
    assert isinstance(assert_type(intersects, numpy.ufunc), numpy.ufunc)


def test_is_ccw():
    assert isinstance(assert_type(is_ccw, numpy.ufunc), numpy.ufunc)


def test_is_closed():
    assert isinstance(assert_type(is_closed, numpy.ufunc), numpy.ufunc)


def test_is_empty():
    assert isinstance(assert_type(is_empty, numpy.ufunc), numpy.ufunc)


def test_is_geometry():
    assert isinstance(assert_type(is_geometry, numpy.ufunc), numpy.ufunc)


def test_is_missing():
    assert isinstance(assert_type(is_missing, numpy.ufunc), numpy.ufunc)


def test_is_prepared():
    assert isinstance(assert_type(is_prepared, numpy.ufunc), numpy.ufunc)


def test_is_ring():
    assert isinstance(assert_type(is_ring, numpy.ufunc), numpy.ufunc)


def test_is_simple():
    assert isinstance(assert_type(is_simple, numpy.ufunc), numpy.ufunc)


def test_is_valid():
    assert isinstance(assert_type(is_valid, numpy.ufunc), numpy.ufunc)


def test_is_valid_input():
    assert isinstance(assert_type(is_valid_input, numpy.ufunc), numpy.ufunc)


def test_is_valid_reason():
    assert isinstance(assert_type(is_valid_reason, numpy.ufunc), numpy.ufunc)


def test_length():
    assert isinstance(assert_type(length, numpy.ufunc), numpy.ufunc)


def test_line_interpolate_point():
    assert isinstance(assert_type(line_interpolate_point, numpy.ufunc), numpy.ufunc)


def test_line_interpolate_point_normalized():
    assert isinstance(
        assert_type(line_interpolate_point_normalized, numpy.ufunc), numpy.ufunc
    )


def test_line_locate_point():
    assert isinstance(assert_type(line_locate_point, numpy.ufunc), numpy.ufunc)


def test_line_locate_point_normalized():
    assert isinstance(
        assert_type(line_locate_point_normalized, numpy.ufunc), numpy.ufunc
    )


def test_line_merge():
    assert isinstance(assert_type(line_merge, numpy.ufunc), numpy.ufunc)


def test_linearrings():
    assert isinstance(assert_type(linearrings, numpy.ufunc), numpy.ufunc)


def test_linestrings():
    assert isinstance(assert_type(linestrings, numpy.ufunc), numpy.ufunc)


def test_make_valid():
    assert isinstance(assert_type(make_valid, numpy.ufunc), numpy.ufunc)


def test_minimum_bounding_circle():
    assert isinstance(assert_type(minimum_bounding_circle, numpy.ufunc), numpy.ufunc)


def test_minimum_bounding_radius():
    assert isinstance(assert_type(minimum_bounding_radius, numpy.ufunc), numpy.ufunc)


def test_minimum_clearance():
    assert isinstance(assert_type(minimum_clearance, numpy.ufunc), numpy.ufunc)


def test_normalize():
    assert isinstance(assert_type(normalize, numpy.ufunc), numpy.ufunc)


def test_offset_curve():
    assert isinstance(assert_type(offset_curve, numpy.ufunc), numpy.ufunc)


def test_oriented_envelope():
    assert isinstance(assert_type(oriented_envelope, numpy.ufunc), numpy.ufunc)


def test_overlaps():
    assert isinstance(assert_type(overlaps, numpy.ufunc), numpy.ufunc)


def test_point_on_surface():
    assert isinstance(assert_type(point_on_surface, numpy.ufunc), numpy.ufunc)


def test_points():
    assert isinstance(assert_type(points, numpy.ufunc), numpy.ufunc)


def test_polygonize():
    assert isinstance(assert_type(polygonize, numpy.ufunc), numpy.ufunc)


def test_polygonize_full():
    assert isinstance(assert_type(polygonize_full, numpy.ufunc), numpy.ufunc)


def test_polygons():
    assert isinstance(assert_type(polygons, numpy.ufunc), numpy.ufunc)


def test_prepare():
    assert isinstance(assert_type(prepare, numpy.ufunc), numpy.ufunc)


def test_registry():
    assert isinstance(assert_type(registry, list[type]), list)
    for item in registry:
        assert isinstance(item, type)


def test_relate():
    assert isinstance(assert_type(relate, numpy.ufunc), numpy.ufunc)


def test_relate_pattern():
    assert isinstance(assert_type(relate_pattern, numpy.ufunc), numpy.ufunc)


def test_remove_repeated_points():
    assert isinstance(assert_type(remove_repeated_points, numpy.ufunc), numpy.ufunc)


def test_reverse():
    assert isinstance(assert_type(reverse, numpy.ufunc), numpy.ufunc)


def test_segmentize():
    assert isinstance(assert_type(segmentize, numpy.ufunc), numpy.ufunc)


def test_set_precision():
    assert isinstance(assert_type(set_precision, numpy.ufunc), numpy.ufunc)


def test_set_srid():
    assert isinstance(assert_type(set_srid, numpy.ufunc), numpy.ufunc)


def test_shared_paths():
    assert isinstance(assert_type(shared_paths, numpy.ufunc), numpy.ufunc)


def test_shortest_line():
    assert isinstance(assert_type(shortest_line, numpy.ufunc), numpy.ufunc)


def test_simplify():
    assert isinstance(assert_type(simplify, numpy.ufunc), numpy.ufunc)


def test_simplify_preserve_topology():
    assert isinstance(assert_type(simplify_preserve_topology, numpy.ufunc), numpy.ufunc)


def test_snap():
    assert isinstance(assert_type(snap, numpy.ufunc), numpy.ufunc)


def test_symmetric_difference():
    assert isinstance(assert_type(symmetric_difference, numpy.ufunc), numpy.ufunc)


def test_symmetric_difference_all():
    assert isinstance(assert_type(symmetric_difference_all, numpy.ufunc), numpy.ufunc)


def test_symmetric_difference_prec():
    assert isinstance(assert_type(symmetric_difference_prec, numpy.ufunc), numpy.ufunc)


def test_to_geojson():
    assert isinstance(assert_type(to_geojson, numpy.ufunc), numpy.ufunc)


def test_to_wkb():
    assert isinstance(assert_type(to_wkb, numpy.ufunc), numpy.ufunc)


def test_to_wkt():
    assert isinstance(assert_type(to_wkt, numpy.ufunc), numpy.ufunc)


def test_touches():
    assert isinstance(assert_type(touches, numpy.ufunc), numpy.ufunc)


def test_unary_union():
    assert isinstance(assert_type(unary_union, numpy.ufunc), numpy.ufunc)


def test_unary_union_prec():
    assert isinstance(assert_type(unary_union_prec, numpy.ufunc), numpy.ufunc)


def test_union():
    assert isinstance(assert_type(union, numpy.ufunc), numpy.ufunc)


def test_union_prec():
    assert isinstance(assert_type(union_prec, numpy.ufunc), numpy.ufunc)


def test_voronoi_polygons():
    assert isinstance(assert_type(voronoi_polygons, numpy.ufunc), numpy.ufunc)


def test_within():
    assert isinstance(assert_type(within, numpy.ufunc), numpy.ufunc)


def test_shapely_error():
    assert issubclass(ShapelyError, Exception)


def test_geos_exception():
    assert issubclass(GEOSException, ShapelyError)


@pytest.fixture
def point():
    return Point(0, 0)


@pytest.fixture
def linestring():
    return LineString([(0, 0), (1, 1)])


class TestGeometry:
    def test_validate_geometry_types(self, point: Geometry, linestring: Geometry):
        """Validate that our point and linestring are indeed Geometry objects."""
        assert isinstance(point, Geometry)
        assert isinstance(linestring, Geometry)

    def test_geom(self, point: Geometry):
        assert isinstance(assert_type(point._geom, int), int)

    def test_geom_prepared(self, point: Geometry):
        assert isinstance(assert_type(point._geom_prepared, int), int)

    def test_eq_dunder(self, point: Geometry, linestring: Geometry):
        assert isinstance(assert_type(point.__eq__(linestring), bool), bool)

    def test_ge_dunder(self, point: Geometry, linestring: Geometry):
        assert isinstance(
            assert_type(point.__ge__(linestring), NotImplementedType),
            NotImplementedType,
        )

    def test_gt_dunder(self, point: Geometry, linestring: Geometry):
        assert isinstance(
            assert_type(point.__gt__(linestring), NotImplementedType),
            NotImplementedType,
        )

    def test_hash_dunder(self, point: Geometry):
        assert isinstance(assert_type(point.__hash__(), int), int)

    def test_le_dunder(self, point: Geometry, linestring: Geometry):
        assert isinstance(
            assert_type(point.__le__(linestring), NotImplementedType),
            NotImplementedType,
        )

    def test_lt_dunder(self, point: Geometry, linestring: Geometry):
        assert isinstance(
            assert_type(point.__lt__(linestring), NotImplementedType),
            NotImplementedType,
        )

    def test_ne_dunder(self, point: Geometry, linestring: Geometry):
        assert isinstance(assert_type(point.__ne__(linestring), bool), bool)


@pytest.fixture
def tree(point: Geometry, linestring: Geometry):
    return STRtree(numpy.asarray([point, linestring]), 10)


@pytest.fixture
def empty_tree():
    return STRtree(numpy.asarray([], dtype=numpy.object_), 10)


class TestSTRtree:
    def test_ptr(self, tree: STRtree):
        assert isinstance(assert_type(tree._ptr, int), int)

    def test_empty_ptr(self, empty_tree: STRtree):
        assert isinstance(assert_type(empty_tree._ptr, int), int)

    def test_count(self, tree: STRtree):
        assert isinstance(assert_type(tree.count, int), int)

    def test_empty_count(self, empty_tree: STRtree):
        assert isinstance(assert_type(empty_tree.count, int), int)
        assert empty_tree.count == 0

    def test_first_arguement_type(self, point: Geometry, linestring: Geometry):
        with pytest.raises(TypeError):
            # Ignore the type here because we are testing known invalid input.
            STRtree([point, linestring], 10)  # type: ignore
        STRtree(numpy.asarray([point, linestring]), 10)

    # TODO: Test query methods with the empty STRtree.
    def test_dwithin(self, tree: STRtree, point: Geometry):
        result = tree.dwithin(numpy.asarray([point]), numpy.ndarray(1, float))
        assert isinstance(assert_type(result, npt.NDArray[numpy.int64]), numpy.ndarray)

        element = result.take(1)  # pyright: ignore[reportUnknownMemberType]
        assert_type(element, numpy.int64)
        assert isinstance(
            element, numpy.int64  # pyright: ignore[reportGeneralTypeIssues]
        )

    def test_nearest(self, tree: STRtree, point: Geometry):
        result = tree.nearest(numpy.asarray([point]))
        assert isinstance(assert_type(result, npt.NDArray[numpy.int64]), numpy.ndarray)

        element = result.take(1)  # pyright: ignore[reportUnknownMemberType]
        assert_type(element, numpy.int64)
        assert isinstance(
            element, numpy.int64  # pyright: ignore[reportGeneralTypeIssues]
        )

    def test_query(self, tree: STRtree, point: Geometry):
        query_geometries = numpy.asarray([point])
        predicate = 0
        result = tree.query(query_geometries, predicate)
        assert isinstance(assert_type(result, npt.NDArray[numpy.int64]), numpy.ndarray)

        element = result.take(1)  # pyright: ignore[reportUnknownMemberType]
        assert_type(element, numpy.int64)
        assert isinstance(
            element, numpy.int64  # pyright: ignore[reportGeneralTypeIssues]
        )

    def test_query_nearest(self, tree: STRtree, point: Geometry):
        query_geometries = numpy.asarray([point])
        max_distance = 1
        exclusive = True
        all_matches = False
        indices, distances = tree.query_nearest(
            query_geometries, max_distance, exclusive, all_matches
        )

        # Test indices response type
        assert isinstance(assert_type(indices, npt.NDArray[numpy.int64]), numpy.ndarray)
        index = indices.take(0)  # pyright: ignore[reportUnknownMemberType]
        assert_type(index, numpy.int64)
        assert isinstance(
            index, numpy.int64  # pyright: ignore[reportGeneralTypeIssues]
        )

        # Test distances response type
        assert isinstance(
            assert_type(distances, npt.NDArray[numpy.float64]), numpy.ndarray
        )
        distance = distances.take(0)  # pyright: ignore[reportUnknownMemberType]
        assert_type(distance, numpy.float64)
        assert isinstance(
            distance, numpy.float64  # pyright: ignore[reportGeneralTypeIssues]
        )


def test_private_setup_signal_checks():
    # Test that "None" does not work as the second argument.
    with pytest.raises(TypeError):
        _setup_signal_checks(10_000, None)  # type: ignore

    main_thread_id = threading.main_thread().ident
    assert isinstance(main_thread_id, int)  # Narrow the type of the main thread id.
    result = _setup_signal_checks(10_000, main_thread_id)
    assert assert_type(result, None) is None

    # Try with a float.
    with pytest.raises(TypeError):
        result = _setup_signal_checks(10_000.0, main_thread_id)  # type: ignore


class TestCountCoordinates:
    def test_must_be_array(self, linestring: Geometry):
        with pytest.raises(TypeError):
            count_coordinates(linestring)  # type: ignore

        with pytest.raises(TypeError):
            count_coordinates([linestring])  # type: ignore

    def test_single_geometry(self, linestring: Geometry):
        result = count_coordinates(numpy.asarray(linestring, dtype=numpy.object_))
        assert isinstance(assert_type(result, int), int)

    def test_multiple_geometries(self, linestring: Geometry, point: Geometry):
        geometries = [linestring, point]
        result = count_coordinates(numpy.asarray(geometries, dtype=numpy.object_))
        assert isinstance(assert_type(result, int), int)

    def test_non_geometry_array(self):
        with pytest.raises(TypeError):
            integers = numpy.asarray([1, 2, 3], dtype=numpy.int64)
            count_coordinates(integers)  # type: ignore

    def test_empty_array(self):
        geometries = []
        result = count_coordinates(numpy.asarray(geometries, dtype=numpy.object_))
        assert isinstance(assert_type(result, int), int)


class TestGetCoordinates:
    def test_must_be_array(self, linestring: Geometry):
        for include_z in [True, False]:
            for return_index in [True, False]:
                with pytest.raises(TypeError):
                    get_coordinates(linestring, include_z, return_index)  # type: ignore

                with pytest.raises(TypeError):
                    get_coordinates(
                        [linestring], include_z, return_index  # type: ignore
                    )

    def test_bool_overload(self, linestring: Geometry):
        # Bool overloads are tricky. You need one for Literal[True] and Literal[False]
        # and bool for them to work.
        for include_z in [True, False]:
            for return_index in [True, False]:
                assert_type(return_index, bool)
                geometries = numpy.asarray(linestring, dtype=numpy.object_)
                result = get_coordinates(geometries, include_z, return_index)
                assert_type(
                    result,
                    npt.NDArray[numpy.float64]
                    | tuple[npt.NDArray[numpy.float64], npt.NDArray[numpy.int64]],
                )

    def test_single_geometry_no_return_index(self, linestring: Geometry):
        for include_z in [True, False]:
            return_index = False
            geometries = numpy.asarray(linestring, dtype=numpy.object_)
            result = get_coordinates(geometries, include_z, return_index)

            assert_type(result, npt.NDArray[numpy.float64])
            assert isinstance(result, numpy.ndarray)
            assert isinstance(result.take(0), numpy.float64)  # pyright: ignore

    def test_single_geometry_return_index(self, linestring: Geometry):
        for include_z in [True, False]:
            return_index = True
            geometries = numpy.asarray(linestring, dtype=numpy.object_)
            coords, indices = get_coordinates(geometries, include_z, return_index)
            assert_type(coords, npt.NDArray[numpy.float64])
            assert isinstance(coords, numpy.ndarray)
            assert str(coords.dtype) == "float64"
            assert isinstance(coords.take(0), numpy.float64)  # pyright: ignore

            assert_type(indices, npt.NDArray[numpy.int64])
            assert isinstance(indices, numpy.ndarray)
            assert str(indices.dtype) == "int64"
            assert isinstance(indices.take(0), numpy.int64)  # pyright: ignore

    # TODO: The 'multiple geometries' tests are almost entirely duplicated code of the
    # single case. Look into conslidating a little.
    def test_multiple_geometries_no_return_index(
        self, linestring: Geometry, point: Geometry
    ):
        for include_z in [True, False]:
            return_index = False
            geometries = numpy.asarray([linestring, point], dtype=numpy.object_)
            result = get_coordinates(geometries, include_z, return_index)
            element = result.take(0)  # pyright: ignore[reportUnknownMemberType]

            assert_type(result, npt.NDArray[numpy.float64])
            assert isinstance(result, numpy.ndarray)
            assert_type(element, numpy.float64)
            assert isinstance(
                element, numpy.float64  # pyright: ignore[reportGeneralTypeIssues]
            )

    def test_multiple_geometries_return_index(
        self, linestring: Geometry, point: Geometry
    ):
        for include_z in [True, False]:
            return_index = True
            geometries = numpy.asarray([linestring, point], dtype=numpy.object_)
            coords, indices = get_coordinates(geometries, include_z, return_index)

            assert_type(coords, npt.NDArray[numpy.float64])
            assert isinstance(coords, numpy.ndarray)
            assert str(coords.dtype) == "float64"
            assert isinstance(coords.take(0), numpy.float64)  # pyright: ignore

            assert_type(indices, npt.NDArray[numpy.int64])
            assert isinstance(indices, numpy.ndarray)
            assert str(indices.dtype) == "int64"
            assert isinstance(indices.take(0), numpy.int64)  # pyright: ignore

    def test_empty_array_no_return_index(self):
        for include_z in [True, False]:
            return_index = False
            geometries = numpy.asarray([], dtype=numpy.object_)
            result = get_coordinates(geometries, include_z, return_index)
            assert isinstance(
                assert_type(result, npt.NDArray[numpy.float64]), numpy.ndarray
            )
            assert str(result.dtype) == "float64"

    def test_empty_array_return_index(self):
        for include_z in [True, False]:
            return_index = True
            geometries = numpy.asarray([], dtype=numpy.object_)
            coords, indices = get_coordinates(geometries, include_z, return_index)

            assert_type(coords, npt.NDArray[numpy.float64])
            assert isinstance(coords, numpy.ndarray)
            assert str(coords.dtype) == "float64"

            assert_type(indices, npt.NDArray[numpy.int64])
            assert isinstance(indices, numpy.ndarray)
            assert str(indices.dtype) == "int64"


class TestSetCoordinates:
    def test_single_geometry(self, point: Geometry):
        geometries = numpy.asarray(point, dtype=numpy.object_)
        coordinates = numpy.array([[1, 1]], dtype=numpy.float64)
        result = set_coordinates(geometries, coordinates)
        assert_type(result, npt.NDArray[numpy.object_])
        assert isinstance(result, numpy.ndarray)
        element = result.take(0)  # pyright: ignore[reportUnknownMemberType]
        assert isinstance(element, Geometry)
        assert id(geometries) == id(result)

    def test_empty_argumnets(self):
        geometries = numpy.asarray([], dtype=numpy.object_)
        coordinates = numpy.array([[]], dtype=numpy.float64)
        result = set_coordinates(geometries, coordinates)
        assert_type(result, npt.NDArray[numpy.object_])
        assert isinstance(result, numpy.ndarray)
        assert str(result.dtype) == "object"
        assert id(geometries) == id(result)

    def test_non_float64(self, point: Geometry):
        geometries = numpy.asarray(point, dtype=numpy.object_)
        coordinates = numpy.array([[1, 1]], dtype=numpy.float32)
        with pytest.raises(TypeError):
            set_coordinates(geometries, coordinates)  # type: ignore
