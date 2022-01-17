import numpy as np
import cv2

from typing import Tuple

BLUE = np.array([255, 0, 0])
YELLOW = np.array([0, 255, 255])
RED = np.array([0, 0, 255])
BLACK = (0, 0, 0)


def create_blank(size: Tuple[int, int]):
    print(size)
    return np.zeros((size[0], size[1], 3)) + 255


def draw_cones(img: np.ndarray, position: Tuple[int, int], color: int) -> None:
    color_value = YELLOW if color else BLUE
    cv2.circle(img, position, 5, color_value)


def f(x, y, z):
    return z == round(x + y, 1)


def draw_track(shape, f, z) -> np.ndarray:
    img = create_blank(
        (
            int((shape[0][1] - shape[0][0]) / shape[0][2]),
            int((shape[1][1] - shape[1][0]) / shape[1][2]),
        )
    )
    for xi, x in enumerate(np.arange(*shape[0])):
        for yi, y in enumerate(np.arange(*shape[1])):
            if f(x, y, z):
                img[yi, xi] = RED

    return img


def draw_start(img, position: Tuple[int, int]) -> np.ndarray:
    cv2.circle(img, position, 3, BLACK, 3)
    img[position] = BLACK
    return img


def display_track(img: np.ndarray):
    cv2.imshow("Track", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


lower = 3
upper = 5

point = 4


class Field:
    __shape = ((0, 0, 0), (0, 0, 0))
    __x_range = 0
    __y_range = 0

    @staticmethod
    def setShape(shape: Tuple[Tuple[int, int, float], Tuple[int, int, float]]):
        Field.__shape = shape
        Field.__x_range = int((shape[0][1] - shape[0][0]) / shape[0][2])
        Field.__y_range = int((shape[1][1] - shape[1][0]) / shape[1][2])

    @staticmethod
    def getIndex(position: Tuple[int | float, int | float]) -> Tuple[int, int]:
        return (
            int((position[0] - Field.__shape[0][0]) / Field.__shape[0][2]),
            int((position[1] - Field.__shape[1][0]) / Field.__shape[1][2]),
        )

    @staticmethod
    def getPosition(index: Tuple[int, int]) -> Tuple[int | float, int | float]:
        return (
            index[0] * Field.__shape[0][2] + Field.__shape[0][0],
            index[1] * Field.__shape[1][2] + Field.__shape[1][0],
        )


if __name__ == "__main__":
    shape = ((-2, 2, 0.01), (-2, 2, 0.01))
    Field.setShape(shape)
    img = draw_track(shape, f, 0)
    img = draw_start(img, Field.getIndex((0, 0)))
    next_cone_distance = 10
    display_track(img)
