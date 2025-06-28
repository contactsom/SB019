import numpy as np

a2 = np.array([0,1,2,3])

x=a2.copy()
y=a2.view()


print("x.base-- ",x.base)
print("y.base-- ",y.base)