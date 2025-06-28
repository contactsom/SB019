import numpy as np


a1 = np.array(34)
a2 = np.array([1,2,3,4,5])
a3 = np.array([[1,2,3,4,5],[11,12,13,14,15]])
a4 = np.array([[[1,2,3,4,5],[11,12,13,14,15],[21,32,23,24,25]]])

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)
print(a4.ndim)