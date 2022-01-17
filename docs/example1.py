from typing import Tuple
import numpy as np
import cv2

SCALE = 1

S = (-3, 0)


def f(x, y, z):
    return z == round(x ** 2 + y ** 2 + x * y, SCALE)


xs = np.arange(-4, 4, 0.01)
ys = np.arange(-4, 4, 0.01)


def create_blank(size: Tuple[int, int]):
    return np.zeros((size[0], size[1], 3)) + 255


img = create_blank((len(xs), len(ys)))

z = 9
for xi, x in enumerate(xs):
    for yi, y in enumerate(ys):
        if f(x, y, z):
            img[yi, xi] = np.array([0, 0, 255])
            if (round(x, SCALE), round(y, SCALE)) == S:
                img[yi, xi] = np.array([0, 0, 0])


cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("./docs/example1.png", img)
