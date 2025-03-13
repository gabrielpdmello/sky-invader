#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from Code.const import WIN_HEIGHT, ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY, COLLISION_DELAY
from Code.entity import Entity
from Code.playerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.collision_delay = COLLISION_DELAY

    def update(self, ):
        pass

    def move(self, axis=False):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.left < WIN_WIDTH - 62:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        # the shot delay must be implemented inside the main game loop, this way it's possible to limit the shot rate while not introducing any delay to the first shot
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LCTRL] or pressed_key[pygame.K_SPACE]:
            return PlayerShot(name=f'Shots/player_shot',
                              position=(self.rect.centerx, (self.rect.centery - self.height)))
