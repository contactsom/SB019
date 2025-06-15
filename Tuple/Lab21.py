# +Ve Index :   0, 1,  2,  3,  4,  5,  6
# Tuple     :( 10, 20, 30, 40, 50, 60, 70 )
# -Ve Index :  -7, -6, -5, -4, -3, -2, -1

myTuple=(10,20,30,40,50,60,70)
print(myTuple[0])
myTuple[0]=100
print(myTuple) # TypeError: 'tuple' object does not support item assignment


