import time
# def decor(func):
#
#     def inner():
#         a = func()
#         multi = a*5
#         return multi
#     return inner
#
# def decor1(func1):
#
#     def inner():
#         b = func1()
#         add = b+5
#         return add
#     return inner
#
# def num():
#     return 10
#
# k = decor(decor1(num))
# print(k())
#
# def divdecor(func):
#     start = time.time()
#     def inner(a,b):
#         if b==0:
#             print("denom should not be 0")
#         else:
#             return func(a,b)
#     end = time.time()
#     #print("divdecore took" + str((end - start)*1000) + "mil sec")
#     return inner
#
# def add(a,b):
#     return a/b
#
# add = divdecor(add)
# print(add)
# print(add(10,2))


def smart_div(f):
    def inner(a,b):
        if b>a:
            a,b = b,a
        return f(a,b)
    return inner



def div(a,b):
    return a/b

div=smart_div(div)
print(div(2,10))