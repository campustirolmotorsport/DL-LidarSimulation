from typing import List, Tuple
from . import Track, Field, Cone

from .cone import generateCones
from ..constants import GREEN
from ..image import Image


class World:
    def __init__(self, track: Track, field: Field) -> None:
        self.track = track
        self.field = field
        self.__cones: List[Tuple[Cone, Cone]] | None = None
        self.__trackImage: Image | None = None
        self.__trackConesImage: Image | None = None

    def trackImage(self) -> Image:
        if self.__trackImage:
            return self.__trackImage.copy()
        blank = self.field.blank()
        for t in self.track.trackRange(self.field.scale):
            x, y = self.field.getPixel(self.track.track(t))
            blank[y, x] = GREEN
        image = Image(blank)
        self.__trackImage = image
        return image

    @property
    def cones(self) -> List[Tuple[Cone, Cone]]:
        if self.__cones is None:
            self.__cones = generateCones(self.track, self.field)
        return self.__cones

    def trackConesImage(self) -> Image:
        if self.__trackConesImage is None:
            image = self.trackImage()

            self.__trackConesImage = image
        return self.__trackConesImage

    @staticmethod
    def addCones(image: Image, cones: List[Tuple[Cone, Cone]]):
        for cone1, cone2 in cones:
            cone1.drawCone(image)
            cone2.drawCone(image)
        return image
