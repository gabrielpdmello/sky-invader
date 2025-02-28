#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.examples.grid import WINDOW_HEIGHT
from pygame.font import Font

from Code.const import LEVEL_FONT_SIZE, LEVEL_FONT_COLOR, WIN_WIDTH, WIN_HEIGHT
from Code.entity import Entity
from Code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.extend(EntityFactory.get_entity('Level1Prop'))
        self.timeout = 20000

    def run(self, ):
        pygame.mixer_music.load(f'./Assets/Sounds/littlerobotsoundfactory__loop_max_power(modified).wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source = ent.surf, dest = ent.rect)
                ent.move('y')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close
                    quit()  # end pygame

            self.level_text(LEVEL_FONT_SIZE, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', LEVEL_FONT_COLOR, (10, 5))
            self.level_text(LEVEL_FONT_SIZE, f'FPS: {clock.get_fps() :.0f}', LEVEL_FONT_COLOR, ((WIN_WIDTH - 70), 5))
            self.level_text(LEVEL_FONT_SIZE, f'Entities: {len(self.entity_list)}', LEVEL_FONT_COLOR, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)