import pytest
from newa_downloader import coordinates


def test_valid_coordinate():
    coordinates.validate_coordinate(5.0, (-1, 8))


def test_invalid_coordinate():
    with pytest.raises(coordinates.CoordinateOutOfRangeError):
        coordinates.validate_coordinate(15.0, (0, 1))
    with pytest.raises(coordinates.CoordinateOutOfRangeError):
        coordinates.validate_coordinate(-10.0, (0, 1))


def test_valid_latitude_pair():
    coordinates.validate_latitude_pair(45,33)


def test_invalid_latitude_pair():
    with pytest.raises(coordinates.CoordinateOutOfRangeError):
        coordinates.validate_latitude_pair(89, 33)

    with pytest.raises(coordinates.CoordinateOutOfRangeError):
        coordinates.validate_latitude_pair(45, -3)

    with pytest.raises(coordinates.CoordinateOutOfRangeError):
        coordinates.validate_latitude_pair(100, -1)

    with pytest.raises(coordinates.LatitudeComparisonError):
        coordinates.validate_latitude_pair(33, 45)


def test_valid_longitude_pair():
    coordinates.validate_longitude_pair(9., 1.)


def test_invalid_longitude_pair():
    with pytest.raises(coordinates.CoordinateOutOfRangeError):
        coordinates.validate_longitude_pair(57, 9)

    with pytest.raises(coordinates.CoordinateOutOfRangeError):
        coordinates.validate_longitude_pair(9, -100)

    with pytest.raises(coordinates.CoordinateOutOfRangeError):
        coordinates.validate_longitude_pair(68, -123)

    with pytest.raises(coordinates.LongitudeComparisonError):
        coordinates.validate_longitude_pair(23, 40)
