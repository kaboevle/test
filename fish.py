import pygame
from vector import *
import random

class Fish:
    def __init__(self,pos,vel,img,border):
        self.__pos = pos
        self.__vel = vel
        self.__img = img
        self.__vec = vel
        self.__border = border

    @property
    def pos(self):
        return self.__pos
    
    def bordercontrol(self):
        if self.__pos.x >800-50 or self.__pos.x<0:
            self.__vec.x = self.__vec.x * -1
        if self.__pos.y >600-50 or self.__pos.y<0:
            self.__vec.y = self.__vec.y * -1
    
    def update(self, flok):
        self.__pos = self.__pos + self.__vel
        self.bordercontrol2()
        self.__vel += self.separtion(flok, 50 , 10)
        self.__vel += self.alignment(flok, 50 , 0.25)
        if self.__vel.x > 3:
            self.__vel.x = random.uniform(0.1,2)
        if self.__vel.x < -3:
            self.__vel.x = random.uniform(-2,-0.1)
        if self.__vel.y > 3:
            self.__vel.y = random.uniform(0.1,2)
        if self.__vel.y < -3:
            self.__vel.y = random.uniform(-2,-0.1)
   
    def draw(self,screen):
        screen.blit(self.__img,(self.__pos.x,self.__pos.y))

    def bordercontrol2(self):
        velocity = self.__vel
        if self.__pos.x < self.__border:
            velocity.x = velocity.x + ((1-self.__pos.x/self.__border)**2)
        
        if self.__pos.y < self.__border:
            velocity.y = velocity.y + ((1-self.__pos.y/self.__border)**2)
        
        if self.__pos.x > 800-self.__border-25:
            velocity.x = velocity.x + ((1-(self.__pos.x-600)/self.__border)**2)*-1
        
        if self.__pos.y > 600-self.__border-25:
            velocity.y = velocity.y + ((1-(self.__pos.y-400)/self.__border)**2)*-1

    def separtion(self,flok,tooclose,separation_factor):
        separation_vector = Vector(0,0)
        for fish in flok:
            if fish != self:
                distance = self.__pos.distance(fish.pos)
                if distance < tooclose:
                    separation_vector += (self.__pos - fish.pos).normalize() / distance
        return(separation_vector * separation_factor)
    
    def alignment(self, flok, visible_distance, alignemt_factor):
        alignment_vector = Vector(0,0)
        count = 0
        for fish in flok:
            if fish != self:
                distance = self.__pos.distance(fish.pos)
                if distance < visible_distance:
                    alignment_vector += fish.__vel
                    count += 1
        if count > 0:
             alignment_vector /= count
             #alignment_vector = (alignment_vector - self.__vel)
             return (alignment_vector.normalize() * alignemt_factor)
        return (alignment_vector)
