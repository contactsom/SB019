'''
active Count()
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
t3=Thread(target=squeres,args=(numbers,))

t1.start()
t2.start()
t3.start()


print("The Number of Active Thread :: ",active_count())
