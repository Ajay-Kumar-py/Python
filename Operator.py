

class duck:
    def walk(self):
        print("thapak thapak thapak thapak")

class horse:
    def walk(self):
        print("takbak takbak takbaktakbak")

def func(obj):
    obj.walk()

d = duck()
func(d)