
# Multiple Returns in a function

def getSum_Sub(a,b):
    sum=a+b
    sub=a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div # It returns 100 Values


output=getSum_Sub(10,20)
print(output) # (30, -10, 200, 0.5)

for a in output:
    print(a)






