#E
import pygame

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
    'Player/1B': 1,
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
    'Player/1B': 5,
    'Enemies/enemy1': 4,
    'Enemies/enemy2': 4,
    'Enemies/enemy3': 4,
    'Enemies/enemy4': 4,
    'Shots/enemy_shot_normal': 6,
    'Shots/enemy_shot_special': 6,
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
    'Enemies/enemy1': 60,
    'Enemies/enemy2': 60,
    'Enemies/enemy3': 60,
    'Enemies/enemy4': 60,
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
    'Enemies/enemy1': 100,
    'Enemies/enemy2': 100,
    'Enemies/enemy3': 200,
    'Enemies/enemy4': 500,
    'Shots/enemy_shot_normal': 0,
    'Shots/enemy_shot_special': 0,
    'Shots/player_shot': 0,
}

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SHOT_DELAY = {
    'Player/1B': 10,
    'Enemies/enemy1': 80,
    'Enemies/enemy2': 80,
    'Enemies/enemy3': 80,
    'Enemies/enemy4': 80,
}

#L

LEVEL_FONT_SIZE = 24
LEVEL_FONT_COLOR = (255, 255, 255) # white

#M
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
SPAWN_RATE = 1000

#W
WIN_WIDTH = 450
WIN_HEIGHT = 600

