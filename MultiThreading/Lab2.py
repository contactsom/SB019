'''
1. Create the Thread Without using any class
'''

from threading import *

def display():
    for i in range(1,11):
        print("Child Thread - ",i)

t=Thread(target=display) # Creating the Thread Object where object name is t
t.start() # Starting the thread

for i in range(1,11):
    print("This is main thread")