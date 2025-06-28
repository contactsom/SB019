import numpy as np


a2 = np.array([1,2,3,4,5,6,7,8,9,10,11])

newArray=a2.reshape(4,3)

print(newArray) # cannot reshape array of size 11 into shape (4,3)
