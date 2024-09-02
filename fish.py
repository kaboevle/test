import pygame
from vector import *

class Fish:
    def __init__(self,pos,vel,img):
        self.pos = pos
        self.vel = vel
        self.img = img
        self.img = pygame.image.load(self.img)
        self.img = pygame.transform.scale(self.img, (50,50))
    
    def update(self):
        self.pos = self.pos + self.vel
        if self.pos.x >800 or self.pos.x<0:
            self.vel.setter(self.vel.x*-1,self.vel.y)
        if self.pos.y >600 or self.pos.y<0:
            self.vel.setter(self.vel.x,self.vel.y*-1)
   
    def draw(self,screen):
        screen.blit(self.img,(self.pos.x,self.pos.y))