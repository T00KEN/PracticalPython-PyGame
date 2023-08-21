import pygame as pg

# Colors add your own if needed, basic colors added.
COLORS = {"black": pg.Color('#000000'), 'white': pg.Color('#FFFFFF'),
          'red': pg.Color('#FF0000'), 'purple': pg.Color('#800080'),
          'blue': pg.Color('#0000FF'), 'yellow': pg.Color('#FFFF00'),
          'gray': pg.Color('#333333'), 'silver': pg.Color('#C0C0C0')}

# Tiles and Screen
TILE_SIZE = 64
VERTICAL_TILE_NUM = 10
HORIZONTAL_TILE_NUM = 12

HEIGHT = VERTICAL_TILE_NUM * TILE_SIZE
WIDTH = HORIZONTAL_TILE_NUM * TILE_SIZE

# Time
FPS = 60
