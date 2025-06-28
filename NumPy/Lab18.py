import numpy as np


a2 = np.array([1, 2, 3, 4, 5])

print("Order pf [a2] :: ",a2.ndim)
print("Element pf a2[4:] :: ",a2[4:]) # [5]
print("Element pf a2[:4] :: ",a2[:4]) #[1 2 3 4]

print("Element pf a2[-3:-1]:: ",a2[-3:-1])
print("Element pf a2[1:5:2] :: ",a2[1:5:2])
print("Element pf a2[::2] :: ",a2[::2])
