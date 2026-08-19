import pygame
from init import *
from constants import *

def show(snake):
    for part in snake:
        pygame.draw.rect(game_display, COLORS.get('White'), (part[0], part[1], CELL_SIZE, CELL_SIZE), 1)                         

def update_screen(direction, snake):
    if direction == 'RIGTH':
        snake.pop(0)
        snake.append([snake[-1][0] + CELL_SIZE, snake[-1][1]])
        return snake
    
    elif direction == 'UP':
        snake.pop(0)
        snake.append([snake[-1][0], snake[-1][1] - CELL_SIZE])