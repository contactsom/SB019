
# Types of Variables in a Function
# 1. Global Variables
# 2. Local Variables


a = 10 # Global Variable
def f1():
    a=900 # Local Variable
    print("Local Variable :: ",a)
    print("Global Variable :: ",globals()['a']) # I want to access the 10 which is Global Value

f1()









