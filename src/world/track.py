from typing import Tuple
from math import sin, cos, pi, atan
import numpy as np
from scipy.misc import derivative

from ..helper import signum
from ..constants import DX

from ..Types import NUMBER


class Track:
    trackLength = 2 * pi
    trackStart = 0

    @staticmethod
    def trackRange(res: NUMBER) -> np.ndarray:
        return np.arange(Track.trackStart, Track.trackLength, res)

    @staticmethod
    def track_x(t: float) -> float:
        return 1 / 2 * sin(t)

    @staticmethod
    def track_y(t: float) -> float:
        return 2 * cos(t)

    @staticmethod
    def track(t: float) -> Tuple[float, float]:
        return (Track.track_x(t), Track.track_y(t))

    @staticmethod
    def degree(t: float) -> float:
        dx = derivative(Track.track_x, t, dx=DX)
        dy = derivative(Track.track_y, t, dx=DX)
        if dx == 0:
            return signum(dy) * pi / 2
        if dy == 0:
            return 0 if signum(dx) > 0 else 180 if signum(dx) < 0 else 0
        return dx / dy + 90
