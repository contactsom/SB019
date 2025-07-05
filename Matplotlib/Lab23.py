import matplotlib.pyplot as pit
import numpy as np

x=np.array([1,2,5,9,10,20,15,19])
y=np.array([2,8,2,10,12,18,12,10])

pit.plot(x)
pit.plot(y)

pit.xlabel("This is my X-Axis")
pit.ylabel("This is my Y-Axis")

pit.show()

