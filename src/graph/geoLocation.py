import math
from src.graph.geoLocationInterface import GeoLocationInterface


class GeoLocation(GeoLocationInterface):

    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self._x = x
        self._y = y
        self._z = z

    def __eq__(self, other: GeoLocationInterface):
        return self._x == other.get_x() and self._y == other.get_y() and self._z == other.get_z()

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def get_z(self) -> float:
        return self._z

    def distance(self, g) -> float:
        dis_x = math.pow(self._x - g.get_x(), 2)
        dis_y = math.pow(self._y - g.get_y(), 2)
        dis_z = math.pow(self._z - g.get_z(), 2)
        return math.sqrt(dis_x + dis_y + dis_z)

    def __repr__(self):
        return f"( x:{self._x}, y:{self._y}, z:{self._z} )"



