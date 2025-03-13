import sys

import pygame
from pygame import Surface, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE, Rect
from pygame.font import Font

from Code.DBProxy import DBProxy
from Code.const import SCORE_POS, SCORE_FONT_COLOR, SCORE_BG_COLOR
from Code.entity import Entity
from Code.entityFactory import EntityFactory


class Score:
    def __init__(self, window: Surface):
        self.window = window
        pass

    def save(self, player_score: int):
        pygame.mixer.music.unload()
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.fill(SCORE_BG_COLOR)
            self.score_text(48, 'GAME OVER', SCORE_FONT_COLOR, SCORE_POS['Title'])
            text = 'ENTER PLAYER NAME (4 CHARACTERS)'
            score = player_score
            self.score_text(20, text, SCORE_FONT_COLOR, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, SCORE_FONT_COLOR, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer.music.unload()
        self.window.fill(SCORE_BG_COLOR)
        self.score_text(48, 'TOP 10 SCORE', SCORE_FONT_COLOR, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE', SCORE_FONT_COLOR, SCORE_POS['Label'])
        self.score_text(20, 'PRESS ESC TO GO TO MENU', SCORE_FONT_COLOR, SCORE_POS['Back'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score= player_score
            self.score_text(20, f'{name}     {score:05d}', SCORE_FONT_COLOR,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
