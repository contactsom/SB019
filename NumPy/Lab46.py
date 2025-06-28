import numpy as np


a1 = np.array( [1,2,3])
a2 = np.array( [4,5,6])

arr=np.concatenate((a1,a2),axis=1)
print(arr)
