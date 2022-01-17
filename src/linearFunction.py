import cv2
import numpy as np
import numpy.typing as npt
from math import sqrt
from typing import Optional, Tuple
from .Types import COLOR, NUMBER, POLAR, POSITION, SCALAR
from .constants import RED
from .image import Image


class LinearFunction:
    def __init__(
        self, matrix: npt.NDArray, start: NUMBER = None, end: NUMBER = None
    ) -> None:
        assert matrix.shape == (2, 2)
        self.start = start
        self.end = end
        self.matrix = matrix

    @property
    def supportVector(self) -> np.ndarray:
        return self.matrix[0]

    @supportVector.setter
    def supportVector(self, vector: npt.NDArray) -> None:
        self.matrix[0] = vector

    @property
    def directionVetor(self) -> np.ndarray:
        return self.matrix[1]

    @directionVetor.setter
    def directionVector(self, vector: npt.NDArray) -> None:
        self.matrix[1] = vector

    def onFunction(self, point: POSITION) -> bool:
        if (self.directionVector == 0).all():
            return point == (0, 0)
        if self.directionVector[0] == 0:
            return self.supportVector[0] == point[0]
        if self.directionVector[1] == 0:
            return self.supportVector[1] == point[1]
        return ((point[0] - self.supportVector[0]) / self.directionVetor[0]) == (
            (point[1] - self.supportVector[1]) / self.directionVetor[1]
        )

    def onLine(self, point: POSITION) -> bool:
        if not (self.start and self.end):
            return self.onFunction(point)
        if self.onFunction(point):
            x = (
                (point[0] - self.supportVector[0]) / self.directionVetor[0]
                if self.directionVetor[0] != 0
                else 0
            )
            y = (
                (point[1] - self.supportVector[1]) / self.directionVetor[1]
                if self.directionVector[1] != 0
                else 0
            )
            t = np.sqrt(x ** 2 + y ** 2)
            if self.start <= t and self.end >= t:
                return True
        return False

    def inRange(self, t: SCALAR) -> bool:
        if not (self.start != None and self.end != None):
            return False
        value = self.value(t)
        if self.start < t and self.end > t:
            return True
        return False

    def key(self, pos: POSITION) -> SCALAR:
        if self.directionVector[0] == 0:
            return (pos[1] - self.supportVector[1]) / self.directionVetor[1]
        if self.directionVetor[1] == 0:
            return (pos[0] - self.supportVector[0]) / self.directionVetor[0]
        t1 = (pos[0] - self.supportVector[0]) / self.directionVetor[0]
        t2 = (pos[1] - self.supportVector[1]) / self.directionVetor[1]
        return t1

    def draw(self, image: Image, field, color: COLOR = RED) -> Image:
        if self.end is not None and self.start is not None:
            point1 = field.getPixel(self.value(self.start))
            point2 = field.getPixel(self.value(self.end))
        else:
            print("Missing Implementation")
            assert False

        cv2.line(image.raw, point1, point2, color)
        return image

    def value(self, t: SCALAR) -> POSITION:
        v = self.supportVector + self.directionVector * (
            t / sqrt(np.sum(self.directionVector ** 2))
        )
        return v[0], v[1]

    def distance(
        self, point: POSITION, t: bool = False
    ) -> Tuple[SCALAR, Optional[SCALAR]]:
        x1, x2 = point
        s1, s2 = self.supportVector
        r1, r2 = self.directionVector
        t = (r1 * x1 + r2 * x2 - r1 * s1 - r2 * s2) / (r1 ** 2 + r2 ** 2)
        d = sqrt(sum((self.value(t) - np.array(point)) ** 2))
        if t:
            return d, t
        return d, None

    @property
    def polar(self) -> POLAR:
        assert self.end and self.start
        r = self.end - self.start
        d = np.arctan(self.directionVector[1] / self.directionVector[0])
        return (r, d)

    def __str__(self) -> str:
        return f"{self.supportVector} + {self.directionVector} * t\n"
