import matplotlib.pyplot as pit
import numpy as np

x=np.array([1,2,5,9,10,20,15,19])
y=np.array([82,80,72,91,52,38,42,30])

font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}
font3={'family':'serif','color':'hotpink','size':25}


pit.title("Roll - Marks ",fontdict=font3,loc='left')
pit.xlabel("Roll Number",fontdict=font1,loc='left')
pit.ylabel("Marks",fontdict=font2,loc='bottom')

pit.plot(x,y)

pit.show()

