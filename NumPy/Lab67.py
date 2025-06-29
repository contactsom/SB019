import numpy as np

mycount=np.char.equal('Simplilearn','ABC')
print(mycount)


mycount1=np.char.equal('Simplilearn','Simplilearn')
print(mycount1)

mycount2=np.char.equal('ABC','abc')
print(mycount2)

mycount3=np.char.equal('ABC','Abc')
print(mycount3)