#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.const import WIN_WIDTH, MENU_TITLE_FONT_SIZE, MENU_TITLE_FONT_COLOR, MENU_OPTION_FONT_COLOR, MENU_OPTION, \
    MENU_OPTION_FONT_SIZE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Assets/Images/Clouds 3/all.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./Assets/Sounds/264778__zagi2__aliens-feast-loop.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(MENU_TITLE_FONT_SIZE, 'Sky', MENU_TITLE_FONT_COLOR, ((WIN_WIDTH/2), 60) )
            self.menu_text(MENU_TITLE_FONT_SIZE, 'Invader', MENU_TITLE_FONT_COLOR, ((WIN_WIDTH/2), 110) )

            for i in range(len(MENU_OPTION)):
                self.menu_text(MENU_OPTION_FONT_SIZE, MENU_OPTION[i], MENU_OPTION_FONT_COLOR, ((WIN_WIDTH / 2), 180 + i * 40))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
