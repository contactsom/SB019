import matplotlib.pyplot as pit
import numpy as np

x1=np.array([1,2,3,4])
y1=np.array([82,80,72,91])

pit.subplot(2,1,1)
pit.plot(x1,y1)
pit.title("SubPlot-1")


x2=np.array([1,2,3,4])
y2=np.array([70,60,50,40])

pit.subplot(2,1,2)
pit.plot(x2,y2)
pit.title("SubPlot-2")

pit.show()

