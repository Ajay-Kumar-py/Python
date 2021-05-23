class student:

    def __init__(self):
        print("hi there !!")

    def sum(self,a=None,b=None,c=None):
        s=0

        if(a!=None and b!=None and c!=None):
            s=a+b+c
            return s
        elif(a!=None and b!=None):
            s=a+b
            return s
        else:
            s=a
            return s

s1=student()
print(s1.sum(2,5,3))



###########################################################
def add(datatype,*arg):

    if datatype == 'int':
        answer = 0

    if datatype == 'str':
        answer = " "

    for x in arg:
        answer = answer + x

    print(answer)

add('int',5,6)
add('int',5,6)












