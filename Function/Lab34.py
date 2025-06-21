
# Types of Variables in a Function
# 1. Global Variables
# 2. Local Variables


a = 10 # Global Variable
def f1():
    a=900
    print(a)

def f2():
    print(a)

def f3():
    global a
    a=777
    print(a)

f1() # 900
f2() # 10
f3() #










