#E
import pygame

ENTITY_SPEED = {
    'moon_and_sea_pixel_art_background/1': 0,
    'moon_and_sea_pixel_art_background/2': 0,
    'moon_and_sea_pixel_art_background/3': 1,
    'moon_and_sea_pixel_art_background/4': 0,
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
    'moon_and_sea_pixel_art_background/1': 1,
    'moon_and_sea_pixel_art_background/2': 1,
    'moon_and_sea_pixel_art_background/3': 1,
    'moon_and_sea_pixel_art_background/4': 1,
    'level1/1': 1,
    'level1/smoke1': 1,
    'level1/smoke2': 1,
    'level1/smoke3': 1,
    'level1/smoke4': 1,
    'Player/1B': 100,
    'Enemies/enemy1': 100,
    'Enemies/enemy2': 100,
    'Enemies/enemy3': 100,
    'Enemies/enemy4': 100,
    'Shots/enemy_shot_normal': 1,
    'Shots/enemy_shot_special': 1,
    'Shots/player_shot': 1,
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

