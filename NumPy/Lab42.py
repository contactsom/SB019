import numpy as np


a2 = np.array( [
                [[10,20,30],[40,50,60]],
                [[11,12,13],[14,15,16]],
                ]
            )


for x in  np.nditer(a2):
    print(x)
