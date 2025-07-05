try:
   print("I am try")
   print(90/0)
except ZeroDivisionError as msg:
    print("1-Exception Have been raised :: ",msg)
else:
    print("I am else")
    print("Else block will get executed when try block does not have any error ")

finally:
    print("I do't care any one I will execute always")
print("I am Statement -5 ")


