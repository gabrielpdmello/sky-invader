#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Code.const import LEVEL_FONT_SIZE, LEVEL_FONT_COLOR, WIN_WIDTH, WIN_HEIGHT, EVENT_ENEMY, SPAWN_RATE_DELAY, \
    ENTITY_SHOT_DELAY, FPS
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
        self.timer = 0
        self.spawn_rate_increase_span = 1
        self.spawn_rate_delay = SPAWN_RATE_DELAY
        pygame.time.set_timer(EVENT_ENEMY, self.spawn_rate_delay)
        self.pause = False

    def run(self, debug=False):
        pygame.mixer.music.load(f'./Assets/Sounds/littlerobotsoundfactory__loop_max_power(modified).wav')
        shot_sound = pygame.mixer.Sound(f'./Assets/Sounds/676322__rubberduck9999__retro-laser-shot.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(80)
        clock = pygame.time.Clock()
        player_score = 0
        while True:
            clock.tick(FPS)
            self.timer += 1000 / FPS
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move('y')
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    ent.shot_delay -= 1
                    if shoot is not None and ent.shot_delay <= 0:
                        ent.shot_delay = ENTITY_SHOT_DELAY[ent.name]
                        self.entity_list.append(shoot)
                        if ent.name == 'Player/1B':
                            pygame.mixer.Sound.play(shot_sound)

                if ent.name == "Player/1B":
                    self.level_text(LEVEL_FONT_SIZE, f'Health: {ent.health}',
                                    LEVEL_FONT_COLOR, (10, (WIN_HEIGHT - 20)))
                    self.level_text(LEVEL_FONT_SIZE, f'Score: {ent.score}',
                                    LEVEL_FONT_COLOR, ((WIN_WIDTH - 10),
                                                       (WIN_HEIGHT - 20)), True)

            # spawn rate delay decreases each minute
            if (self.timer / 1000) / 60 >= self.spawn_rate_increase_span:
                self.spawn_rate_delay *= 0.8
                self.spawn_rate_increase_span += 1
                pygame.time.set_timer(EVENT_ENEMY, int(self.spawn_rate_delay))
                self.entity_list.append(EntityFactory.get_entity('HP'))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close
                    quit()  # end pygame
                if event.type == EVENT_ENEMY:
                    choice = random.choices(['Enemy1', 'Enemy2', 'Enemy3'], weights=[5, 3, 1])
                    self.entity_list.append(EntityFactory.get_entity(choice[0]))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.pause = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    if pygame.mixer.music.get_volume() > 0:
                        pygame.mixer.music.set_volume(0)
                    else:
                        pygame.mixer.music.set_volume(80)

            while self.pause:
                pygame.mixer.music.pause()
                self.level_text(50, 'PAUSED', LEVEL_FONT_COLOR, (WIN_WIDTH / 2, WIN_HEIGHT / 2), False,
                                True)
                pygame.display.flip()
                while self.pause:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()  # Close
                            quit()  # end pygame
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                            self.pause = False
                            pygame.mixer.music.unpause()

            # check if player is alive each iteration
            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True
                    ent.collision_delay -= 1
                    player_score = ent.score

            # finish level loop if player dies, and return score
            if not found_player:
                return player_score

            self.level_text(LEVEL_FONT_SIZE, f'FPS: {clock.get_fps() :.0f}', LEVEL_FONT_COLOR, ((WIN_WIDTH - 70), 5))
            self.level_text(LEVEL_FONT_SIZE, f'Time: {self.timer / 1000:.1f}s', LEVEL_FONT_COLOR, (10, 5))

            if debug:
                self.level_text(LEVEL_FONT_SIZE, f'Entities: {len(self.entity_list)}', LEVEL_FONT_COLOR, (10, 25))
                self.level_text(LEVEL_FONT_SIZE, f'Spawn rate (ms): {self.spawn_rate_delay}', LEVEL_FONT_COLOR,
                                (10, 45))

            pygame.display.flip()

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, sub_width=False,
                   sub_half_width=False):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        # if true, subtracts text width from position to avoid text outside of window
        if sub_width:
            text_rect: Rect = text_surf.get_rect(left=(text_pos[0] - text_surf.get_width()), top=text_pos[1])
        # if true, subtracts halt the text width to center text
        elif sub_half_width:
            text_rect: Rect = text_surf.get_rect(left=(text_pos[0] - text_surf.get_width() / 2), top=text_pos[1])
        else:
            text_rect: Rect = text_surf.get_rect(left=(text_pos[0]), top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
