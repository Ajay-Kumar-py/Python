
class A:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(self.a)
        print(self.b)
class B(A):

    def demo(self):
        # self.c = c
        # self.d = d
        #
        pass

ob = B(80,90)