from vector import *
from fish import *
import pygame
import random 


class flok:
    def __init__(self,antal,img):
         self.fishs = []
         self.n = 0
         self.antal = antal
         self.__img = img
         self.__img = pygame.image.load(self.__img)
         self.__img = pygame.transform.scale(self.__img, (25,25))
         

    def updatering(self):
          while(self.n<self.antal):
              position = Vector(random.uniform(200,600),random.uniform(200,400))
              velocity = Vector(random.uniform(-2,2),random.uniform(-2,2))
              i = Fish(position,velocity,self.__img,(random.uniform(50,100)))
              self.fishs.append(i)
              self.n +=1

    def tegn(self,screen):
         for x in self.fishs:
            x.update(self.fishs)
            x.draw(screen)