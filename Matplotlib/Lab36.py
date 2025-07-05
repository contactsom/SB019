import matplotlib.pyplot as pit
import numpy as np

x1=np.array([1,2,3,4,70,60,50,40])
y1=np.array([82,80,70,60,50,40,72,91])

color=np.array(["red","blue","green","yellow","pink","black","orange","purple"])
pit.scatter(x1,y1,c=color)

pit.show()

