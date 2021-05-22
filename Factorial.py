

n = int(input("Enter a no : "))

fact = 1
for i in range(1,n+1):
    fact*=i

print(fact)

def fact(x):

    if x==1:
        return 1

    else:
        return x*fact(x-1 )

x = int(input("Enter the no : "))
print("Factorial of no : ",fact(x))