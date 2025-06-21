
# Types of Variables in a Function
# 1. Global Variables
# 2. Local Variables


a = 10 # Global Variable
def f1():
    a=900
    print(a)

def f2():
    global a
    a = 777
    print(a)

def f3():
    print(a)

def f4():
   print(a)

f1() # 900
f2() # 777
f3() # 777
f4() # 777










