try:
    a = int(input("Enter First Number :: "))
    b = int(input("Enter Second Number :: "))
    print(a/b)
except ZeroDivisionError as msg:
    print("Exception Have been raised :: ",msg)

print("I am Statement -5 ")


