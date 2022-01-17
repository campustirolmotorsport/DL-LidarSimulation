from typing import List
import cv2
import numpy as np
from scipy.misc import derivative
from scipy.integrate import quad
from math import sqrt
from ..helper import *
from .track import Track
from .field import Field
from ..image import Image
from ..linearFunction import LinearFunction


class Cone:
    def __init__(
        self, field: Field, position: POSITION, color: COLOR, radius: SCALAR = 0.03
    ) -> None:
        self.field = field
        self.position = position
        self.color = color
        self.radius = radius

    def drawCone(self, image: Image) -> None:
        """Function to draw the cone to a given image.

        Returns:
            IMAGE: Reference for the updated image containing the drawn cone
        """
        cv2.circle(
            image.raw,
            self.field.getPixel(self.position),
            self.field.scaleToIndex(self.radius),
            self.color,
        )

    def hitCone(self, f: LinearFunction) -> Tuple[bool, POSITION]:
        if f.onLine(self.position):
            return True, self.position
        distance, t = f.distance(self.position, t=True)
        t = t if t else 0
        if self.radius <= distance and f.onLine(f.value(t)) and t >= 0:
            return True, f.value(t)
        return False, (0, 0)


def nextConeTrackPosition(
    time: float,
    track: Track,
    distance: float,
    step: float,
) -> Tuple[float, POSITION]:
    def arcLength(x1, x2):

        value, error = quad(
            lambda x: sqrt(
                derivative(track.track_x, x, dx=DX) ** 2
                + derivative(track.track_y, x, dx=DX) ** 2
            ),
            x1,
            x2,
        )
        return value

    d = 0
    n = time
    while d < distance:
        n += step
        d = arcLength(time, n)
    return n, track.track(n)


def conePosition(
    time: float, track: Track, field: Field, distance: float
) -> Tuple[Cone, Cone]:
    x, y = track.track(time)
    dx = derivative(track.track_x, time, dx=DX)
    dy = derivative(track.track_y, time, dx=DX)
    d = sqrt(dy ** 2 + dx ** 2)
    cone1 = (x - dy * distance / d, y + dx * distance / d)
    cone2 = (x - dy * -distance / d, y + dx * -distance / d)
    return Cone(field, cone1, YELLOW), Cone(field, cone2, BLUE)


def generateCones(track: Track, field: Field) -> List[Tuple[Cone, Cone]]:
    cones: List[Tuple[Cone, Cone]] = []
    t = track.trackStart
    while t <= track.trackLength:
        cones.append(conePosition(t, track, field, DISTANCE_CONES))
        t, _ = nextConeTrackPosition(t, track, DISTANCE_TRACK_CONE, 0.01)
    return cones
