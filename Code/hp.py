import pygame

from Code.const import ENTITY_SPEED, HP_COLOR, HP_FONT_SIZE
from Code.entity import Entity


class HP(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def update(self, ):
        pass

    def move(self, axis = False):
        self.rect.centery += ENTITY_SPEED[self.name]