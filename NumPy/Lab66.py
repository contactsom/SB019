import numpy as np

mycount=np.char.isnumeric('Simplilearn')
print(mycount)


mycount1=np.char.isnumeric('123Simplilearn')
print(mycount1)


mycount2=np.char.isnumeric('123')
print(mycount2)
