
# Filter Function
# Syntex
# filter(function,sequence)

def isEven(x):
    if x%2==0:
        return True
    else:
        return False


output1=isEven(4)
print(output1)

output2=isEven(5)
print(output2)

mylist=[5,4,6,8,2,7,9]
l=list(filter(isEven,mylist))
print(l)










