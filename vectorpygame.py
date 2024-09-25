import pygame
from vector import *
from fish import *
from Stime import *

def game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True
    fisk = flok(50,'Fisk.png')
    while running:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
        screen.fill((0, 128, 255))
        fisk.updatering()
        fisk.tegn(screen)
        pygame.display.flip()
        clock.tick(60)  
game()
pygame.quit()