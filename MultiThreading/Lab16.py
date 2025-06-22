'''
Synchronization
If multiple threads are executing simutaneously then there may be a chance of teh data inconsistancy prpblem
'''

import time
from threading import *

l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print("Good Evening:",end='')
        time.sleep(2)
        print(name)
    l.release()


t1=Thread(target=wish,args=("Pranay",))
t1.start()
t2=Thread(target=wish,args=("Florance",))
t2.start()
t3=Thread(target=wish,args=("Kashish",))
t3.start()