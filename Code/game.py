#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.level import Level
from Code.menu import Menu
from Code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from Code.score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, debug=False):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:  # play
                level = Level(self.window, 'Level1')
                if debug:
                    player_score = level.run(debug=True)
                else:
                    player_score = level.run()

                score.save(player_score)

            elif menu_return == MENU_OPTION[1]:  # score
                score.show()

            elif menu_return == MENU_OPTION[2]:  # quit
                pygame.quit()
                quit()
