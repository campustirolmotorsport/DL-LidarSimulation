import cv2
from . import *
from .image import Image
from typing import Any


def display_image(image: Image, name: str = "Frame", scale: float = 1) -> None:
    shape = image.shape
    scaleImage = cv2.resize(image.raw, (int(shape[0] * scale), int(shape[1] * scale)))
    print(scaleImage.shape)
    cv2.imshow(name, scaleImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def drawStart(image: Image, position: POSITION, field: Any) -> Image:
    x, y = field.getPixel(position)
    image.raw[y, x] = BLACK
    return image


def signum(number: NUMBER) -> int:
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0
