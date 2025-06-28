import numpy as np


a2 = np.array([[1, 2, 3, 4, 5],[11, 12, 13, 14, 15]])

print("Order pf [a2] :: ",a2.ndim)
print("Element pf a2[1,1:4] :: ",a2[1,1:4])
print("Element pf a2[0:4,2] :: ",a2[0:4,2])

print("Element pf a2[0:2,2]:: ",a2[0:2,2])
print("Element pf a2[0:2,1:4] :: ",a2[0:2,1:4])