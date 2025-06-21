
# Multiple Returns in a function

def getSum_Sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub


sumOutput,subOutput=getSum_Sub(10,20)
print("Sum Is ",sumOutput)
print("Sub Is ",subOutput)




