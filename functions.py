import pygame
from init import *
from constants import *
from random import randint

def show(snake):
    for part in snake:
        pygame.draw.rect(game_display, COLORS.get('White'), ((part[0], part[1], CELL_SIZE, CELL_SIZE)), 1) 

def update_screen(direction, snake):
    snake.pop(0)
    
    if direction == 'RIGHT':
        if snake[-1][0] > 19 * CELL_SIZE:
            snake.append([0, snake[-1][1]])
        else:
            snake.append([snake[-1][0] + CELL_SIZE, snake[-1][1]])
        
    elif direction == 'UP':
        if snake[-1][1] < CELL_SIZE:
            snake.append([snake[-1][0], 20 * CELL_SIZE])
        
        else:
            snake.append([snake[-1][0], snake[-1][1] - CELL_SIZE])
    
    elif direction == 'DOWN':
        if snake[-1][1] > 19 * CELL_SIZE:
            snake.append([snake[-1][0], 0])
            
        else:
            snake.append([snake[-1][0], snake[-1][1] + CELL_SIZE])
        
    elif direction == 'LEFT':
        if snake[-1][0] < CELL_SIZE:
            snake.append([20 * CELL_SIZE, snake[-1][1]])
        
        else:
            snake.append([snake[-1][0] - CELL_SIZE, snake[-1][1]])
    
           
    
    return snake