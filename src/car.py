from typing import List
import cv2
import numpy as np
from math import cos, sin

from .Types import CAR_POSITION, POLAR, POSITION
from .image import Image
from .world import Field
from .lidar.lidar import Lidar
from .world import World


class Car:
    def __init__(self, start: CAR_POSITION, field: Field, lidar: Lidar) -> None:
        self.position = start
        self.field = field
        self.lidar = lidar
        self.color = (40, 90, 200)
        self.radius = 8
        self.thickness = 1

    def move(self, position: CAR_POSITION):
        self.position = position

    def draw(self, image: Image) -> Image:
        pixel = self.field.getPixel(self.position[:2])
        pt1 = (
            int(pixel[0] + cos(self.position[2]) * (-self.radius // 2)),
            int(pixel[1] + sin(self.position[2]) * (-self.radius // 2)),
        )
        pt2 = (
            int(pixel[0] + cos(self.position[2]) * (self.radius // 2)),
            int(pixel[1] + sin(self.position[2]) * (self.radius // 2)),
        )
        cv2.circle(
            image.raw,
            self.field.getPixel(self.position[:2]),
            self.radius,
            self.color,
            self.thickness,
        )
        cv2.arrowedLine(
            image.raw, pt1, pt2, self.color, thickness=self.thickness, tipLength=0.5
        )
        return image

    def scan(self, world: World) -> List[POLAR]:
        return self.lidar.scan(self.position, world)

    def drawScan(self, image: Image, world: World) -> Image:
        return self.lidar.draw(image, self.position, world)
