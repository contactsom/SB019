
# Multiple Returns in a function

def getSum_Sub(a,b):
    sum=a+b
    sub=a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div


sumOutput,subOutput,mulOutput,divOutput=getSum_Sub(10,20)
print("Sum Is ",sumOutput)
print("Sub Is ",subOutput)
print("Mul Is ",mulOutput)
print("Div Is ",divOutput)




