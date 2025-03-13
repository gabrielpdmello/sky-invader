#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.const import WIN_WIDTH, MENU_TITLE_FONT_SIZE, MENU_TITLE_FONT_COLOR, MENU_OPTION_FONT_COLOR, MENU_OPTION, \
    MENU_OPTION_FONT_SIZE, MENU_OPTION_FONT_COLOR_SELECTED
from Code.entity import Entity
from Code.entityFactory import EntityFactory


class Menu:
    def __init__(self, window):
        self.window = window
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('MenuBg'))

    def run(self):
        sel_menu_option = 0
        pygame.mixer_music.load('./Assets/Sounds/264778__zagi2__aliens-feast-loop.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move('x')

            self.menu_text(MENU_TITLE_FONT_SIZE, 'Sky', MENU_TITLE_FONT_COLOR, ((WIN_WIDTH / 2), 60))
            self.menu_text(MENU_TITLE_FONT_SIZE, 'Invader', MENU_TITLE_FONT_COLOR, ((WIN_WIDTH / 2), 130))

            for i in range(len(MENU_OPTION)):
                if i == sel_menu_option:
                    self.menu_text(MENU_OPTION_FONT_SIZE, MENU_OPTION[i], MENU_OPTION_FONT_COLOR_SELECTED,
                                   ((WIN_WIDTH / 2), 240 + i * 60))
                else:
                    self.menu_text(MENU_OPTION_FONT_SIZE, MENU_OPTION[i], MENU_OPTION_FONT_COLOR,
                                   ((WIN_WIDTH / 2), 240 + i * 60))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if sel_menu_option < len(MENU_OPTION) - 1:
                            sel_menu_option += 1
                        else:
                            sel_menu_option = 0
                    if event.key == pygame.K_UP:
                        if sel_menu_option > 0:
                            sel_menu_option -= 1
                        else:
                            sel_menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[sel_menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
