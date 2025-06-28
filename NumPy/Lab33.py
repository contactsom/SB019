import numpy as np

# Create an array with 5 dim
# Using a Vector 1,2,3,4
# and verify that last dimension has the value 4
a2 = np.array([1,2,3,4],ndmin=5)


print(a2)
print("a2.shape-- ",a2.shape)