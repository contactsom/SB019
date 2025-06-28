import numpy as np


# Create an array of 5 dimension and verify with 5 element
a2 = np.array([1,2,3,4,5],ndmin=5)


print(a2) # [[[[[1 2 3 4 5]]]]]
print("Number of Dimension :: ",a2.ndim)
