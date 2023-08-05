from dataclasses import dataclass
from typing import Protocol, Tuple

LATITUDE_RANGE = (31.807278,72.17796)
LONGITUDE_RANGE = (-19.420776,46.992065)

class CoordinateOutOfRangeError(ValueError):
    def __init__(self, range: Tuple[float, float]):
        super().__init__(f"Coordinate out of range. Range is {range}. ")

class LatitudeComparisonError(ValueError):
    def __init__(self, north: float, south: float):
        msg = f"North latitude ({north})must be bigger than south latitude {south}."
        super().__init__(msg)

class LongitudeComparisonError(ValueError):
    def __init__(self, east: float, west: float):
        msg = f"East longitude ({east}) must be bigger than western longitude. ({west})"
        super().__init__(msg)



def validate_latitude(latitude: float):
    validate_coordinate(latitude, LATITUDE_RANGE)


def validate_longitude(longitude: float):
    validate_coordinate(longitude, LONGITUDE_RANGE)


def validate_latitude_pair(north: float, south: float):
    if north < south:
        raise LatitudeComparisonError(north, south)
    validate_latitude(north)
    validate_latitude(south)


def validate_longitude_pair(east: float, west: float):
    if east < west:
        raise LongitudeComparisonError(east, west)
    validate_longitude(east)
    validate_longitude(west)


def validate_coordinate(coordinate: float, coordinate_range: Tuple[float, float]):
    if coordinate <= coordinate_range[0]:
        raise CoordinateOutOfRangeError(coordinate_range)
    if coordinate >= coordinate_range[1]:
        raise CoordinateOutOfRangeError(coordinate_range)


class Coordinates(Protocol):
    def get_end_string(self): ...
    def get_dict(self): ...
    def validate_inputs(self): ...


@dataclass
class DataPoint(Coordinates):
    latitude: float
    longitude: float

    def get_end_string(self):
        return "get-data-point"

    def validate_inputs(self):
        validate_latitude(self.latitude)
        validate_longitude(self.longitude)

    def get_dict(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
        }


@dataclass
class BoundingBox(Coordinates):
    south_bound_latitude: float
    north_bound_latitude: float
    west_bound_longitude: float
    east_bound_longitude: float

    def get_end_string(self):
        return "get-data-bbox"

    def get_dict(self):
        return {
            "southBoundLatitude": self.south_bound_latitude,
            "northBoundLatitude": self.north_bound_latitude,
            "westBoundLongitude": self.west_bound_longitude,
            "eastBoundLongitude": self.east_bound_longitude,
        }

    def validate_inputs(self):
        validate_latitude_pair(self.south_bound_latitude, self.north_bound_latitude)
        validate_longitude_pair(self.east_bound_longitude, self.west_bound_longitude)

