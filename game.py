import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT= 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(screen, (255, 0, 0), (400, 300, 50, 50))
    
    pygame.display.update()
    

