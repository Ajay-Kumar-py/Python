def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner
#@str_upper
def print_str():
    return "good morning"

d= str_upper(print_str)
print(d())

print("#######################################")

def div_decorate(func):
    def inner(a,b):
        if a<b:
            print("inside inner")
            a,b = b,a
        return func(a,b)##it will execute a function
    return inner
@div_decorate
def div(a,b):
    return a/b

#div = div_decorate(div)
print(div(80,4))
#print(div(4,2))

print("################################")

