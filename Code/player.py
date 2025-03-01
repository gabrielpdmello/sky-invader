#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from Code.const import WIN_HEIGHT, ENTITY_SPEED, WIN_WIDTH
from Code.entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def update(self, ):
        pass

    def move(self, axis = False):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.left < WIN_WIDTH - 62:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass