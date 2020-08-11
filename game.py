import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

player_position = [400, 300]
player_size=50

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(screen, (255, 0, 0), (player_position[0], player_position[1], player_size, player_size))
    
    pygame.display.update()
    

