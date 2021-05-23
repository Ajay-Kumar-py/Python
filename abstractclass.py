
from abc import ABC, abstractmethod

class animal(ABC):

    def move(self):
        pass

class human(animal):
    def move(self):
        print("i can walk")

class snake(animal):
    def move(self):
        print("i can crawl")

class dog(animal):
    def move(self):
        print("i can bark")

class lion(animal):
    def move(self):
        print("i can roar")


h =human()
h.move()

print("/////////////////////////////////////////////")

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class square(shape):

    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

#sh =shape()
sq = square(5)
print(sq.area())
print(sq.perimeter())
rec = rectangle(5,4)
print(rec.area())
print(rec.perimeter())
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

from abc import *
class Car(ABC):
    def __init__(self, name):
        self.name = name
        print(self.name)

    def color(self):
        self.col = "Green"

    @abstractmethod
    def wheel(self):
        pass

    @abstractmethod
    def sile(self):
        pass


class Jumbo:
    def wheel(self):
        print("wheel is no differnet")

    def sile(self):
        print("silence")


s = Jumbo()
s.wheel()
s.sile()
s1 = Car("Shesman")




