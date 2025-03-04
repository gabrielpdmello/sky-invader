#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame

from Code.const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./Assets/Images/' + name + '.png').convert_alpha()
        self.width = self.surf.get_width()
        self.height = self.surf.get_height()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.destroyed_by = 'None'
        self.score = ENTITY_SCORE[self.name]

    @abstractmethod
    def move(self, axis):
        pass