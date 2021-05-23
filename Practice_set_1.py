
from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("Its running")


class programmer:
    def write(self,other):
        other.read()
class demo:
    def read(self):
        print("I'm reading")

ob = laptop()
pg = programmer()
dm=demo()

pg.write(dm)
ob.process()