from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def setter(self, x, y):
        self.__x = x
        self.__y = y
    def getter(self):
        return(self.__x, self.__y)
    def __add__(self,Plus):
        return Vector(self.__x + Plus.__x, self.__y + Plus.__y)
    def __str__(self):
        return str(self.__x) + " " + str(self.__y)
    def __sub__(self,sub):
        return Vector(self.__x - sub.__x, self.__y - sub.__y)
    def __mul__(self,multi):
        return Vector(self.__x * multi, self.__y * multi)
    def getlenght(self):
        return(sqrt(self.__x**2+self.__y**2))
    def scallar(self,scal):
        return(self.__x * scal.__x +self.__y * scal.__y)
    def __truediv__(self,div):
        return Vector(self.__x / div, self.__y / div)
    def normalize(self):
        return self/self.getlenght()
    def dividere(self,diver):
        return Vector(self.__x / diver, self.__y / diver)
    def distance(self,dis):
        return (sqrt((self.__x - dis.__x)**2+(self.__y - dis.__y)**2))
    
    @property
    def x(self):
        return(self.__x)
    
    @property
    def y(self):
        return(self.__y)
    
    @x.setter
    def x(self,x):
        self.__x = x
    @y.setter
    def y(self,y):
        self.__y = y