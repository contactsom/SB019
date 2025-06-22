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
doubles(numbers)
squeres(numbers)

print("Total Time taken ::",time.time()-beginingTime)
