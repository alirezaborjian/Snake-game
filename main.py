import pygame
import sys
from init import *
from functions import *

clock = pygame.time.Clock()
food_position = food_generator(snake)
while True:
    game_display.fill(COLORS.get('Black'))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            
    show(snake, food_position)
    snake, food_position = update_screen(direction, snake, food_position)
    pygame.display.update()
    clock.tick(SPEED)