import numpy as np

from abc import ABC
from typing import List
from math import sin, cos, pi, sqrt

from numpy.core.numerictypes import ScalarType
from ..Types import CAR_POSITION, ORIENTATION, POLAR, POSITION, SCALAR
from ..world import World, Cone
from ..linearFunction import LinearFunction
from ..helper import signum
from ..image import Image


class Lidar(ABC):
    """An abstruct Lidar class for defining custom Lidar.
    The Lidar class provides a methode called `scan` to generate Lidar Data.

    Args:
        ABC ([type]): [description]
    """

    def __init__(
        self,
        degree: int = 180,
        resolution: float = 1,
        range: float = 0.5,
        orientation: float = 0,
    ) -> None:
        """
        Args:
            degree (int, optional): Scanning angle of the Lidar. Defaults to 180.
            resolution (float, optional): Distance between each laserray in Degree. Defaults to 1°.
            range (float, optional): The maximum range of a laser ray in Meter. Defaults to 2m.
            orientation (float, optional): Rotation of the 0-Position of the Lidar verses the Car orientation in Degree. Defauls to -90°
        """
        self.degree = degree
        self.resolution = resolution
        self.range = range
        self.orientation = orientation

    def scan(self, position: CAR_POSITION, world: World) -> List[POLAR]:
        """Methode to generate Lidar Data in Polar-Coordinates.

        Args:
            position (POSITION): position of the Lidar in context of the Funktion.
            world (World): world object to describe the context the Lidar is in.

        Returns:
            List[POLAR]: Returns a List of Polar Coordinates as result of the scan.
        """

        rays = self._rays(position, world)
        return list(map(lambda x: x.polar, rays))

    def _rays(self, position: CAR_POSITION, world: World) -> List[LinearFunction]:
        cones = filter(
            lambda x: self.__distancePoints(position[:2], x.position) <= self.range,
            np.array(world.cones).reshape(-1),
        )
        cones = sorted(
            cones,
            key=lambda x: self.__distancePoints(position[:2], x.position),
        )
        rays: List[LinearFunction] = []
        print(position)
        for degree in np.arange(0, self.degree, self.resolution):
            print(degree)
            ray = self._ray(position, (degree + position[2]) % 360)
            hit = self._hit(ray, cones)
            ray.start = 0
            ray.end = ray.key(hit)
            rays.append(ray)
        return rays

    def draw(self, image: Image, position: CAR_POSITION, world: World) -> Image:
        for ray in self._rays(position, world):
            ray.draw(image, world.field)
        return image

    def __distancePoints(self, point1: POSITION, point2: POSITION) -> SCALAR:
        return sqrt(np.sum((np.array(point1) - point2) ** 2))

    def _ray(self, position: CAR_POSITION, lidarDegree: float) -> LinearFunction:
        """Methode to gernerate a single Laser Scan

        Args:
            position (POSITION): Position of scan origin.
            lidarDegree (float): Degree of the laser according to internal orientation.
        Returns:
            float: Length of laserray, between `0`-`self.range`.
        """
        degree = (sum([position[2], self.orientation, lidarDegree]) % 360) * (pi / 180)
        direction = round(sin(degree), 5), round(cos(degree), 5)
        matrix = np.array([position[0:2], direction])

        return LinearFunction(matrix, 0, self.range)

    def _hit(self, f: LinearFunction, cones: List[Cone]) -> POSITION:
        for cone in cones:
            hit, pos = cone.hitCone(f)
            if hit:
                return pos
        return f.value(self.range)
