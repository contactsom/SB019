'''
Without Multi Threading
'''

import time
from threading import *

def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("doubles:",2*n)

def squeres(numbers):
    for n in numbers:
        time.sleep(1)
        print("squeres:",n*n)

numbers=[1,2,3,4,5,6]
beginingTime=time.time()

t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squeres,args=(numbers,))

t1.start()
t2.start()
print("---------------")
t1.join()
t2.join()
print("Total Time taken ::",time.time()-beginingTime)

print("Name of the Main Thread :: ",current_thread().name)
print("Name of the First Thread :: ",t1.name)
print("Name of the Second Thread :: ",t2.name)