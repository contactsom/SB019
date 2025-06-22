'''
3. Create the Thread without extending Thread class
'''

from threading import *

class Lab4:
    def display(self):
        for i in range(1,11):
            print("I am Child Thread-2")


obj=Lab4()
t=Thread(target=obj.display())
t.start()

for i in range(1,11):
    print("This is main thread")


