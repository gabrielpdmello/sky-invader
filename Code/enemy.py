#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Code.const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
from Code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, axis = False):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top > WIN_HEIGHT + self.height:
            self.rect.top = -self.height
            self.rect.left = random.randint(0, WIN_WIDTH -40)