#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Code.background import Background
from Code.const import WIN_WIDTH, WIN_HEIGHT
from Code.enemy import Enemy
from Code.hp import HP
from Code.player import Player
from Code.prop import Prop


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'MenuBg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Menu/{i + 1}', (0, 0)))
                    list_bg.append(Background(f'Menu/{i + 1}', (1065, 0)))
                return list_bg
            case 'Level1Bg':
                list_bg = [Background(f'level1/1', (0, 0)),
                           Background(f'level1/1', (0, -WIN_HEIGHT))]
                return list_bg
            case 'Level1Prop':
                list_prop = []
                for i in range (4):
                    list_prop.append(Prop(f'level1/smoke{i + 1}', (random.randint(-80, (WIN_WIDTH - 80)), (-WIN_HEIGHT + i * 150))))
                return list_prop
            case 'Player':
                return Player('Player/1B', ((WIN_WIDTH / 2 - 32), (WIN_HEIGHT - 100)))
            case 'HP':
                return HP('HP', ((random.randint(0, WIN_WIDTH -80)), -400))
            case 'Enemy1':
                return Enemy('Enemies/enemy1', ((random.randint(0, WIN_WIDTH -80)), -400))
            case 'Enemy2':
                return Enemy('Enemies/enemy2', ((random.randint(0, WIN_WIDTH -80)), -400))
            case 'Enemy3':
                return Enemy('Enemies/enemy3', ((random.randint(0, WIN_WIDTH -80)), -400), True)
