


try:
    print("I m in try block")
    x1=int(input("Enter a no"))
    x2=int(input("Enter a second no"))
    z =x1/x2

except ZeroDivisionError as e:
    print("I m in except block",e)

else:
    print("i m in else block")
    print(z)
finally:
    x1=0
    x2=0
    print("out of try,except,else and finally")