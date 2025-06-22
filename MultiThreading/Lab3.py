'''
2. Create the Thread by extending Thread class
'''

from threading import *

class Lab3(Thread):
    def run(self):
        for i in range(10):
            print("Child Thread-1")

t=Lab3()
t.start()


for i in range(1,11):
    print("This is main thread")


