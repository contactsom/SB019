# Constructor Overloading

class Lab3:
    def __init__(self):
        print("No Arg Constructor ")

    def __init__(self,a):
        print("One Arg Constructor ")

    def __init__(self, a,b):
        print("Two Arg Constructor ")


#obj1=Lab3()
#obj1=Lab3(10)
obj1=Lab3(10,20)