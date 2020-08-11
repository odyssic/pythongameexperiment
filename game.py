import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
<<<<<<< HEAD

player_position = [400, 300]
player_size=50
=======
RED = (255, 0, 0)
>>>>>>> 22c9a70115d177ea4d8ce18852cd0492ffff7a64

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

<<<<<<< HEAD
    pygame.draw.rect(screen, (255, 0, 0), (player_position[0], player_position[1], player_size, player_size))
=======
    pygame.draw.rect(screen, RED, (400, 300, 50, 50))
>>>>>>> 22c9a70115d177ea4d8ce18852cd0492ffff7a64
    
    pygame.display.update()
    

