import numpy as np

from ..helper import drawStart
from ..world import World
from ..car import Car
from ..image import Image


class Options:
    def __init__(
        self, track=True, cones=True, car=True, lidar=False, start=True
    ) -> None:
        self.track = track
        self.cones = cones
        self.car = car
        self.lidar = lidar
        self.start = start


class Simulation:
    def __init__(self, world: World, car: Car) -> None:
        self.world = world
        self.car = car

    def lidarImage(self):
        scan = self.car.scan(self.world)

    def generateImage(
        self,
        options: Options = Options(),
    ) -> Image:
        if options.track:
            image = self.world.trackImage()
        else:
            image = Image(self.world.field.blank())
        if options.cones:
            image = World.addCones(image, self.world.cones)
        if options.car:
            image = self.car.draw(image)
        if options.start:
            image = drawStart(image, self.world.track.track(0), self.world.field)
        if options.lidar:
            image = self.car.drawScan(image, self.world)
        return image
