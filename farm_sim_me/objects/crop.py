
import random
import pygame
from pygame.typing import RectLike

from .tile import Tile
from ..assets import assets

class Crop(Tile):

    def __init__(self, pos: RectLike):
        super().__init__(assets.crop1, pos)
        self._stage = 0

    def update(self):
        if self._stage < 2 and random.random() < 0.0083:
            self._stage += 1
            
            if self._stage == 1:
                self.image = assets.crop2
            elif self._stage == 2:
                self.image = assets.crop3

    def can_harvest(self):
        return self._stage == 2