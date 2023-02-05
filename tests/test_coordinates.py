import numpy as np
import numpy.typing as npt
import pytest
from shapely.coordinates import transform
from shapely.geometry.point import Point
from typing_extensions import assert_type


@pytest.fixture
def point() -> Point:
    return Point(0, 0)


class TestTransform:
    def test_transform_single(self, point: Point):
        transformed = transform(point, lambda x: x + 1)
        assert isinstance(assert_type(transformed, Point), Point)

    def test_transform_many(self, point: Point):
        transformed = transform([point, point], lambda x: x + 1)
        assert isinstance(assert_type(transformed, npt.NDArray[np.object_]), np.ndarray)
        assert str(transformed.dtype) == "object"

    def test_transform_array_like_type(self, point: Point):
        # Just make sure none of these throw an error or a type error.
        transform([point, point], lambda x: x + 1)
        transform((point, point), lambda x: x + 1)
        transform(np.asarray((point, point)), lambda x: x + 1)
        transform(np.asarray((point, point), dtype=np.object_), lambda x: x + 1)

        with pytest.raises(TypeError):
            transform((p for p in [point, point]), lambda x: x + 1)  # type: ignore
