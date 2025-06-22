'''
join()
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


t1.daemon = True

t1.start()
t2.start()

t1.join(4)
t2.join(3)


i=enumerate()
for x in i:
   print("Thread Name ::",x.name,"Thread ID ::",x.ident," Is Alive ::",x.is_alive()," Is Demon ::",x.daemon)

print("The Number of Active Thread :: ",active_count())

