#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

from Code.const import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT
from Code.entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, axis):
        if axis == 'x':
            self.rect.centerx -= ENTITY_SPEED[self.name]
            if self.rect.right <= 0:
                self.rect.left = WIN_WIDTH
        elif axis =='y':
            self.rect.centery += ENTITY_SPEED[self.name]
            if self.rect.top >= WIN_HEIGHT:
                self.rect.bottom = 0
