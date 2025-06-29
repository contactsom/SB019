import numpy as np

mycount=np.char.not_equal('Simplilearn','ABC')
print(mycount)


mycount1=np.char.not_equal('Simplilearn','Simplilearn')
print(mycount1)

mycount2=np.char.not_equal('ABC','abc')
print(mycount2)

mycount3=np.char.not_equal('ABC','Abc')
print(mycount3)