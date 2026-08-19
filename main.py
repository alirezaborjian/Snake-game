import pygame
import sys
from init import *
from functions import *

clock = pygame.time.Clock()

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
            
    show(snake)
    snake = update_screen(direction, snake)
    pygame.display.update()
    clock.tick(SPEED)