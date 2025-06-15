
# Defination of the Function

def getMySum(*values): # You are accepting the one or more than one value
    sum=0
    for x in values:
        sum=sum+x
    return sum


value=getMySum(10)
print(value)

value1=getMySum(10,20)
print(value1)

value2=getMySum(10,20,30)
print(value2)

value3=getMySum(10,20,30,50)
print(value3)