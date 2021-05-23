
class student:

    name = "Ajay"
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno


    def show(self):
        print(self.name,self.rollno)

    class Laptop:


        def __init__(self):
            self.brand = "HP"
            self.cpu  ="i5"
            self.ram  = "8gb"

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = student("Ajay",12)
print(s1.show())
lap= student.Laptop()
lap.show()