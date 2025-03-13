import pygame

# C

COLLISION_DELAY = 90 # 90 / 60fps = 1,5s

# E

ENTITY_DAMAGE = {
    'Menu/1': 0,
    'Menu/2': 0,
    'Menu/3': 0,
    'Menu/4': 0,
    'level1/1': 0,
    'level1/smoke1': 0,
    'level1/smoke2': 0,
    'level1/smoke3': 0,
    'level1/smoke4': 0,
    'Player/1B': 1, # player must cause damage to enemy shot
    'HP': 0,
    'Enemies/enemy1': 20,
    'Enemies/enemy2': 20,
    'Enemies/enemy3': 20,
    'Enemies/enemy4': 20,
    'Shots/enemy_shot_normal': 20,
    'Shots/enemy_shot_special': 20,
    'Shots/player_shot': 20,
}

ENTITY_SPEED = {
    'Menu/1': 0,
    'Menu/2': 0,
    'Menu/3': 1,
    'Menu/4': 0,
    'level1/1': 2,
    'level1/smoke1': 3,
    'level1/smoke2': 3,
    'level1/smoke3': 3,
    'level1/smoke4': 3,
    'Player/1B': 6,
    'HP': 4,
    'Enemies/enemy1': 4,
    'Enemies/enemy2': 3,
    'Enemies/enemy3': 8,
    'Shots/enemy_shot_normal': 6,
    'Shots/enemy_shot_special': 12,
    'Shots/player_shot': 10,
}

ENTITY_HEALTH = {
    'Menu/1': 1,
    'Menu/2': 1,
    'Menu/3': 1,
    'Menu/4': 1,
    'level1/1': 1,
    'level1/smoke1': 1,
    'level1/smoke2': 1,
    'level1/smoke3': 1,
    'level1/smoke4': 1,
    'Player/1B': 100,
    'HP': 1,
    'Enemies/enemy1': 40,
    'Enemies/enemy2': 100,
    'Enemies/enemy3': 60,
    'Shots/enemy_shot_normal': 1,
    'Shots/enemy_shot_special': 1,
    'Shots/player_shot': 1,
}

ENTITY_SCORE = {
    'Menu/1': 0,
    'Menu/2': 0,
    'Menu/3': 0,
    'Menu/4': 0,
    'level1/1': 0,
    'level1/smoke1': 0,
    'level1/smoke2': 0,
    'level1/smoke3': 0,
    'level1/smoke4': 0,
    'Player/1B': 0,
    'HP': 0,
    'Enemies/enemy1': 100,
    'Enemies/enemy2': 500,
    'Enemies/enemy3': 1000,
    'Shots/enemy_shot_normal': 0,
    'Shots/enemy_shot_special': 0,
    'Shots/player_shot': 0,
}

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SHOT_DELAY = {
    'Player/1B': 10,
    'Enemies/enemy1': 80,
    'Enemies/enemy2': 100,
    'Enemies/enemy3': 40,
}

# F
FPS = 60

# H
HP_COLOR = (0, 156, 0) # green
HP_FONT_SIZE = 32

# L

LEVEL_FONT_SIZE = 24
LEVEL_FONT_COLOR = (255, 255, 255) # white

# M
MENU_TITLE_FONT_COLOR = (18, 206, 219) # light blue
MENU_TITLE_FONT_SIZE = 100
MENU_OPTION_FONT_COLOR = (255, 255, 255) # white
MENU_OPTION_FONT_COLOR_SELECTED = (255, 255, 0) # yellow
MENU_OPTION_FONT_SIZE = 45
MENU_OPTION = (
    'PLAY',
    'SCORES',
    'EXIT'
)

# S
SPAWN_RATE = 1500

# W
WIN_WIDTH = 450
WIN_HEIGHT = 600

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             'Back': ((WIN_WIDTH / 2), (WIN_HEIGHT - 30)),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }

SCORE_FONT_SIZE = 30
SCORE_FONT_COLOR = (255, 255, 255) # white
SCORE_BG_COLOR = (50, 50, 50) # dark grey