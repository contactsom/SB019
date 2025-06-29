import numpy as np

a=np.array(['geek','Simplilearn','Student','Simpl'])
mycount=np.char.rfind(a,'Simpl')
print(mycount)

mycount1=np.char.rfind(a,'S')
print(mycount1)