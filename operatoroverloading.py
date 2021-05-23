

class student:

    def __init__(self,m1,m2):
        self.m1 =m1
        self.m2 =m2

    def __add__(self, other):
        k1 = self.m1 + other.m1
        k2 =self.m2 + other.m2
        s3 = student(k1,k2) ##s3 is object here
        return s3

    def __gt__(self, other):
        r1 =self.m1+self.m2
        r2 = other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} '    '{}'.format(self.m1,  self.m2)

s1 =student(58,69)
s2 = student(44,22)

s3 =s1+s2
print(s3.m2)

if s1>s2:
    print("They wins")
else:
    print("s2 wins")

print(s1)


