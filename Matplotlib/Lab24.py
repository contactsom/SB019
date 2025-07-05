import matplotlib.pyplot as pit
import numpy as np

x=np.array([1,2,5,9,10,20,15,19])
y=np.array([82,80,72,91,52,38,42,30])

pit.plot(x)
pit.plot(y)

pit.title("Roll - Marks ")
pit.xlabel("Roll Number")
pit.ylabel("Marks")

pit.show()

