#!/usr/bin/python
# -*- coding: utf-8 -*-

from Code.const import ENTITY_SPEED
from Code.entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, axis):
        if axis == 'x':
            self.rect.centerx -= ENTITY_SPEED[self.name]
            if self.rect.right <= 0:
                self.rect.left = self.width - 5  # -5 to remove gap
        elif axis =='y':
            self.rect.centery += ENTITY_SPEED[self.name]
            if self.rect.top >= self.height:
                self.rect.bottom = 0
