import pygame
from constants import *

pygame.init()
game_display = pygame.display.set_mode(WINDOWS_SIZE)
pygame.display.set_caption(GAME_TITLE)
snake = [[0, (WINDOWS_SIZE[0] // 2) - CELL_SIZE], [CELL_SIZE, (WINDOWS_SIZE[0] // 2) - CELL_SIZE], [2 * CELL_SIZE, (WINDOWS_SIZE[0] // 2) - CELL_SIZE]]
direction = 'RIGHT'
