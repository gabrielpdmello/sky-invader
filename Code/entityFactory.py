#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.background import Background
from Code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'MenuBg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Images/moon_and_sea_pixel_art_background/{i + 1}', (0, 0)))
                    list_bg.append(Background(f'Images/moon_and_sea_pixel_art_background/{i + 1}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level1Bg':
                list_bg = []
                list_bg.append(Background(f'Images/level1/1', (0, 0)))
                list_bg.append(Background(f'Images/level1/1', (0, -WIN_HEIGHT)))
                return list_bg
