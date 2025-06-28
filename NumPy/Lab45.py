import numpy as np


a1 = np.array( [[11,12],[13,14]])
a2 = np.array( [[10,20],[30,40]])

arr=np.concatenate((a1,a2),axis=1)
print(arr)
