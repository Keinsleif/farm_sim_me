import pygame
from pygame import Surface
from pygame.typing import RectLike

from ..shared import ToolTypes

class Tile:
    def __init__(self, img: Surface, pos: RectLike):
        self.image = img
        self._pos = pos

    def update(self, dt: int):
        pass

    def draw(self, screen: Surface):
        screen.blit(self.image, self._pos)

    def action(self, tool: ToolTypes):
        pass
