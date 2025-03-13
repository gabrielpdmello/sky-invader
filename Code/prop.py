#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from Code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from Code.entity import Entity


class Prop(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, axis):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT:
            self.rect.bottom = 0
            self.rect.left = random.randint(-80, (WIN_WIDTH - 80))
