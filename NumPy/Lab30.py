import numpy as np

a2 = np.array([0,1,2,3])

x=a2.view()
print(x)

a2[0]=99 # Assiging the 0th indcx with 99
print(x)
