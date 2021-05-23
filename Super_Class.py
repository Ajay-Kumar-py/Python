

class A:

    def __init__(self):
        self.L  = 10
        self.B = 20
        print(self.L, self.B)
    def feat(self):
        print("hi ")

class B:

    def __init__(self):
        self.C = 30
        self.D = 40

        print(self.C, self.D)

class C(A,B):

    def __init__(self):
        super().__init__()
        self.E = 50
        self.F = 60
        print(self.E,self.F)
        super().feat()

ob = C()
