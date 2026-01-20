from enum import Enum
import pygame
from pygame import Surface
from pygame.typing import RectLike

from farm_sim_me.objects.crop import Crop

from . import tile
from ..assets import assets
from ..shared import ToolTypes

class FarmLandStatus(Enum):
    LAND = 0
    TILLED = 1
    HYDRATED = 2
    PLANTED = 3

class FarmLand(tile.Tile):
    def __init__(self, pos: RectLike):
        self._land_img = assets.land
        self._tilled_img = assets.tilled
        self._hydrated_img = assets.hydrated
        super().__init__(self._land_img, pos)
        self.status = FarmLandStatus.LAND
        self.crop = None

    def update(self):
        if self.crop is not None:
            self.crop.update()
    
    def draw(self, screen):
        if self.status == FarmLandStatus.LAND:
            self.image = self._land_img
        elif self.status == FarmLandStatus.TILLED:
            self.image = self._tilled_img
        elif self.status == FarmLandStatus.HYDRATED:
            self.image = self._hydrated_img
        elif self.status == FarmLandStatus.PLANTED:
            self.image == self._hydrated_img
        super().draw(screen)

        if self.status == FarmLandStatus.PLANTED and self.crop != None:
            self.crop.draw(screen)

    def action(self, tool: ToolTypes):
        if self.status is FarmLandStatus.LAND and tool is ToolTypes.HOE:
            self.status = FarmLandStatus.TILLED
        elif self.status is FarmLandStatus.TILLED and tool is ToolTypes.WATERING:
            self.status = FarmLandStatus.HYDRATED
        elif self.status is FarmLandStatus.HYDRATED and tool is ToolTypes.SEED:
            self.crop = Crop(self._pos)
            self.status = FarmLandStatus.PLANTED
        elif self.status is FarmLandStatus.PLANTED and self.crop is not None and self.crop.can_harvest() and tool is ToolTypes.HARVEST:
            self.status = FarmLandStatus.LAND
            self.crop = None
