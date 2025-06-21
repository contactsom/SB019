
# Recursive Function
# Factorial in Maths

def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

output=factorial(5)
print(output)










