from SETTINGS import *
import pygame
from numba.core import types
from numba.typed import Dict
from numba import int32

_ = False
matrix_map = [
    # 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 1
    [1, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, 1],  # 2
    [1, _, 2, 2, _, _, _, _, _, 2, 2, 2, _, _, _, 3, _, _, _, _, 4, _, _, 1],  # 3
    [1, _, _, _, _, _, _, _, _, _, _, 2, 2, _, _, _, 3, _, _, _, _, _, _, 1],  # 4
    [1, _, 2, 2, _, _, _, _, _, _, _, _, 2, _, 4, _, _, 3, _, _, _, 4, _, 1],  # 5
    [1, _, _, _, _, _, 4, _, _, 2, 2, _, 2, _, _, _, _, _, _, 4, _, _, _, 1],  # 6
    [1, _, 3, _, _, _, 2, _, _, 2, _, _, 2, _, _, _, 4, _, _, _, _, 4, _, 1],  # 7
    [1, _, _, 3, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],  # 8
    [1, _, 3, _, _, _, _, _, _, _, 3, _, _, 3, 3, _, _, _, _, 3, 3, _, _, 1],  # 9
    [1, _, 3, _, _, _, 3, 3, _, 3, _, _, _, 3, 3, _, _, _, _, 2, 3, _, _, 1],  # 10
    [1, _, _, _, _, 3, _, 3, _, _, 3, _, _, _, _, _, _, _, _, _, _, _, _, 1],  # 11
    [1, _, 4, _, 3, _, _, _, _, 3, _, _, 2, _, _, _, _, _, _, _, _, 2, _, 1],  # 12
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, 2, _, _, _, _, _, _, 2, 2, _, 1],  # 13
    [1, _, _, 4, _, _, _, _, 4, _, _, _, _, 2, 2, 2, 2, 2, 2, 2, 2, _, _, 1],  # 14
    [1, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, _, _, _, _, _, _, _, 1],  # 15
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 16
]

WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
mini_map = set()
collision_walls = []
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char:
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 1:
                world_map[(i * TILE, j * TILE)] = 1
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = 2
            elif char == 3:
                world_map[(i * TILE, j * TILE)] = 3
            elif char == 4:
                world_map[(i * TILE, j * TILE)] = 4

#
