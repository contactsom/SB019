import sys


class Car:
    pass


c1=Car()

Obj1=c1
Obj2=c1
Obj3=c1
Obj4=c1

print(sys.getrefcount(c1))