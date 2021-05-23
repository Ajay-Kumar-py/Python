

def topen():

    yield 5
    yield 6
    yield 7
    yield 8

values = topen()
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)

dict={}

def top_ten_square():
    n = 1

    while n <= 10:

        sq = n**2
        dict[n]=sq
        yield sq
        n+=1

all_square = top_ten_square()

for i in all_square:
    print(i)

print(dict)
