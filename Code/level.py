#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.const import LEVEL_FONT_SIZE, LEVEL_FONT_COLOR, WIN_WIDTH, WIN_HEIGHT, EVENT_ENEMY, SPAWN_RATE, \
    ENTITY_SHOT_DELAY
from Code.enemy import Enemy
from Code.entity import Entity
from Code.entityFactory import EntityFactory
from Code.entityMediator import EntityMediator
from Code.player import Player


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.extend(EntityFactory.get_entity('Level1Prop'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout = 20000
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_RATE)

    def run(self, ):
        pygame.mixer_music.load(f'./Assets/Sounds/littlerobotsoundfactory__loop_max_power(modified).wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source = ent.surf, dest = ent.rect)
                ent.move('y')
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    ent.shot_delay -= 1
                    if shoot is not None and ent.shot_delay <= 0:
                        ent.shot_delay = ENTITY_SHOT_DELAY[ent.name]
                        self.entity_list.append(shoot)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close
                    quit()  # end pygame
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(LEVEL_FONT_SIZE, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', LEVEL_FONT_COLOR, (10, 5))
            self.level_text(LEVEL_FONT_SIZE, f'FPS: {clock.get_fps() :.0f}', LEVEL_FONT_COLOR, ((WIN_WIDTH - 70), 5))
            self.level_text(LEVEL_FONT_SIZE, f'Entities: {len(self.entity_list)}', LEVEL_FONT_COLOR, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)