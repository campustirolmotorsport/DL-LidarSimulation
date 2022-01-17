from . import Lidar


class Lidar1(Lidar):
    def __init__(self, resolution: float = 1, range: float = 2) -> None:
        super().__init__()
