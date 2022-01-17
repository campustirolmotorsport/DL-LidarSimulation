from typing import List, Tuple
import numpy as np
import cv2


class Image:
    # ToDo: Specify Type for numpy array
    def __init__(self, data: np.ndarray) -> None:
        self.raw = data
        self.shape = data.shape

    def save(self, path: str) -> None:
        cv2.imwrite(path, self.raw)

    def show(self, name: str = "Image"):
        cv2.imshow(name, self.raw)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def copy(self):
        return Image(self.raw.copy())

    @staticmethod
    def blank(size: Tuple[int, int]) -> np.ndarray:
        return np.zeros((size[0], size[1]), dtype=np.uint8) + np.uint8(255)
