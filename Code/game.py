#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.level import Level
from Code.menu import Menu
from Code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            pygame.init()
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]: # play
                level = Level(self.window, 'Level1')
                level_return = level.run()  # level_return is used to change levels. Since there's only 1 level for now,
                # this won't be used

            elif menu_return == MENU_OPTION[1]:  # score
                pass

            elif menu_return == MENU_OPTION[2]: # quit
                pygame.quit()
                quit()
            else:
                pass