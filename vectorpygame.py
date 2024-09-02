import pygame
from vector import *
from fish import *

def game():
    position = Vector(1,1)
    velocity = Vector(1,1)
    fishs = []
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True
    n = 0
    while(n<10):
        i = n
        i = Fish(position,velocity,'Fisk.png')
        position = Vector(n*50 + 1,n*50 + 1)
        velocity = Vector(n*2 +1,n*2+1)
        fishs.append(i)
        n +=1
    while running:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
        screen.fill((0, 128, 255))
        for x in fishs:
            x.update()
            x.draw(screen)
        pygame.display.flip()
        clock.tick(60)  
game()
pygame.quit()