from math import pi
import numpy as np
from .world.cone import *
from .helper import drawStart
from .world.track import Track


def drawFunction(image: Image, track: Track, field: Field) -> Image:
    for t in track.trackRange(field.scale):
        position = track.track(t)
        x, y = field.getPixel(position)
        image.raw[y, x] = RED
    return image


def drawCones(image: Image, track: Track, field: Field) -> Image:
    cones = generateCones(track, field)
    for cone1, cone2 in cones:
        cone1.drawCone(image)
        cone2.drawCone(image)
    return image
    # cv2.circle(img, field.getIndex(cone1.position), 3, YELLOW)
    # cv2.circle(img, field.getIndex(cone2.position), 3, BLUE)


def createVideo(image: Image, path: str, field: Field):
    fourcc = 0x7634706D
    out = cv2.VideoWriter(path, fourcc, 30, field.size)
    for t in np.arange(0, 2 * pi, 0.01):
        position = Track.track(t)
        x, y = field.getPixel(position)
        image.raw[y, x] = RED
        out.write(image.raw)
    out.release()


if __name__ == "__main__":
    size = (500, 500)
    space: SPACE = ((-2.5, 2.5), (-2.5, 2.5), 0.01)
    field = Field(size, space)
    image = Image(field.blank())
    drawFunction(image, Track(), field)
    drawStart(image, Track.track(0), field)
    drawCones(image, Track(), field)
    # createVideo("video.mp4", field)
    display_image(image)
