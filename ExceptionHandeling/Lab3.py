inputA=10
inputB=0
try:
    c = inputA / inputB  # ZeroDivisionError: division by zero
    print(c)
except ZeroDivisionError:
    print("Any number can not be devisable by Zero")

