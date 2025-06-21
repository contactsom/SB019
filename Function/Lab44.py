from functools import *


# Reduce Function
# Syntex
# reduce(function,sequence)

mylist=[5,4,6,8,2,7,9]
result=reduce(lambda x,y:x+y,mylist)
print(result)

result1=reduce(lambda x,y:x*y,mylist)
print(result1)




