import numpy as np
from src.simulation.simulation import Options, Simulation
from src.lidar.lidar import Lidar
from src.world import Field, Track, World
from src.Types import *
from src.helper import display_image, display_image
from src.car import Car

if __name__ == "__main__":
    size = (500, 500)
    space: SPACE = ((-2.5, 2.5), (-2.5, 2.5), 0.01)
    field = Field(size, space)
    world = World(Track(), field)
    car = Car((*Track.track(0), Track.degree(0)), field, Lidar())
    simulation = Simulation(world, car)
    image = simulation.generateImage(Options(lidar=True))
    display_image(image, scale=3)
