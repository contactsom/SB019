try:
    a = int(input("Enter First Number :: "))
    b = int(input("Enter Second Number :: "))
    print(a/b)
except ZeroDivisionError as msg:
    print("1-Exception Have been raised :: ",msg)

except ValueError as msg:
    print("2-Exception Have been raised :: ",msg)
print("I am Statement -5 ")


