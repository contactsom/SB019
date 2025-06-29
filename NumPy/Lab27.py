
import numpy as np

a2 = np.array(['2', '3'], dtype='i')  # Removed 'a'

newa2 = a2.astype('i')

print("Value of a2 :: ", newa2)
print("Data Type [a2] :: ", newa2.dtype)
