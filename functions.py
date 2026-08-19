import pygame
import sys
from init import *
from constants import *
from random import randint

def show(snake, food_position):
    for part in snake:
        pygame.draw.rect(game_display, COLORS.get('White'), ((part[0], part[1], CELL_SIZE, CELL_SIZE)), 1) 
    
    pygame.draw.rect(game_display, COLORS.get('Red'), (food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))
    
def update_screen(direction, snake, food_position):
    
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
    
    if  not food_position == snake[-1]:
        snake.pop(0)
    else:
        food_position = food_generator(snake)    
    
    if snake[-1] in snake[:-1]:
        pygame.quit()
        sys.exit
    
    return snake, food_position

def food_generator(snake):
    food_position = [randint(0, 19) * CELL_SIZE, randint(0, 19) * CELL_SIZE]
    
    while food_position in snake:
        food_position = [randint(0, 19) * CELL_SIZE, randint(0, 19) * CELL_SIZE]
    
    return food_position
