import pygame
import sys
from init import *
from functions import *
direction = 'UP'
clock = pygame.time.Clock()

while True:
    game_display.fill(COLORS.get('Black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    show(snake)
    snkae = update_screen(direction, snake)
    pygame.display.update()
    clock.tick(5)