import numpy as np


# Create an array of 5 dimension and verify with 5 element
a2 = np.array(
            [
                [
                 [1, 2, 3, 4, 5],[11,12,13,14,15],[21,22,23,24,25]
                ],
                [
                 [31, 32, 33, 34, 35],[41,42,43,44,45],[51,52,53,54,55]
                ]
            ]
             )


print("Order pf [a2] :: ",a2.ndim)
print("a2[0] :: ",a2[0])
print("a2[0,1] :: ",a2[0,1])
print("a2[0,1,2] :: ",a2[0,1,2])
