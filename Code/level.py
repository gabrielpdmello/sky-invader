#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

import pygame
from pygame import Surface

from Code.entity import Entity
from Code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source = ent.surf, dest = ent.rect)
                ent.move('y')
            pygame.display.flip()
