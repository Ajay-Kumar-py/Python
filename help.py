
class A():
    def __init__(self):
        self.name = "Ajay"
        self.age = 28
        print(self.name,self.age)
        print("A init")

    def feature1(self):
        print("Feature1 is working")


    def feature2(self):
        print("Feature2 is working")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")

#
a1 = B()
a1.feature1()
print(a1.name)
print(a1.age)

# Python program to demonstrate error if we
# forget to invoke __init__() of parent.

# class A:
#     def __init__(self, n='Rahul'):
#         self.name = n
#
#
# class B(A):
#     def __init__(self, roll):
#         self.roll = roll
#
#
# object = B(23)
# print(object.name)

# class Person(object):
#
#     # Constructor
#     def __init__(self, name):
#         self.name = name
#
#         # To get name
#
#     def getName(self):
#         return self.name
#
#         # To check if this person is employee
#
#     def isEmployee(self):
#         return False
#
#
# # Inherited or Sub class (Note Person in bracket)

