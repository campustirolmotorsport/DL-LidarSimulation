from typing import Any
from ..Types import *
import numpy as np


class Field:
    """Handles computation between Function Space and Image Space."""

    def __init__(self, size: SIZE, space: SPACE) -> None:
        """[summary]

        Args:
            size (SIZE): Size of the image space
            space (SPACE): Size of the function space and resolution.
        """
        assert size[0] == int((space[0][1] - space[0][0]) / space[2])
        assert size[1] == int((space[1][1] - space[1][0]) / space[2])
        self.size = size
        self.space = space
        self.scale: float = space[2]

    # ToDo: Specify Type for numpy array
    @staticmethod
    def createBlank(size: SIZE) -> np.ndarray:
        return np.zeros((size[0], size[1], 3), dtype=np.uint8)

    # ToDo: Specify Type for numpy array
    def blank(self) -> np.ndarray:
        return np.zeros((self.size[0], self.size[1], 3), dtype=np.uint8)

    def getPixel(self, position: POSITION) -> PIXEL:
        return (
            int((position[0] - self.space[0][0]) / self.scale),
            int((position[1] - self.space[1][0]) / self.scale),
        )

    def getPosition(self, index: PIXEL) -> POSITION:
        return (
            index[0] * self.scale + self.space[0][0],
            index[1] * self.scale + self.space[1][0],
        )

    def scaleToIndex(self, number: SCALAR) -> INDEX:
        return int(number / self.scale)

    def scaleToScalar(self, index: INDEX) -> SCALAR:
        return index * self.scale
