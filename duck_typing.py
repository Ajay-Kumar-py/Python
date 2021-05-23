class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno =rollno
        self.lap = self.laptop
    def show(self):
        print(self.name,self.rollno)
        #self.lap.show1()

    class laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "I5"
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = student("ajay",34)
s2 = student("abhi",24)
s2.show()
#s2.show()

class redmi:

    def specs(self):
        print("Good in Camera !!")
        print("Good in game performance")

class apple:

    def specs(self):
        print("single sim phone")
        print("good for slo-mo camera")


class mobile:

    def func(self,other):
        other.specs()

red = redmi()
mo = mobile()
mo.func(red)

#lap = student.laptop()
#lap.show()