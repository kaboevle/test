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
        return Vector(self.__x * multi.__x, self.__y * multi.__y)
    def getlenght(self):
        return(sqrt(self.__x**2+self.__y**2))
    def scallar(self,scal):
        return(self.__x * scal.__x +self.__y * scal.__y)
    @property
    def x(self):
        return(self.__x)
    
    @property
    def y(self):
        return(self.__y)

Nyvector = Vector(4,6)
print(Nyvector)
HeltNyVector = Vector(2,4)
print(HeltNyVector)
PlusVector = Nyvector + HeltNyVector
print(PlusVector)
subVector = Nyvector - HeltNyVector
print(subVector)
mulVector = Nyvector * HeltNyVector
print(mulVector)
print(Nyvector.getlenght())
print(HeltNyVector.getlenght())
print(Nyvector.scallar(HeltNyVector))