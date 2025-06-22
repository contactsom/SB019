class MethodOverloading:
    def m1(self):
        print("I am no Argument Method")

    def m1(self,a):
        print("I am One Argument Method")

    def m1(self, a,b):
        print("I am Two Argument Method")


methodOverloading=MethodOverloading()
#methodOverloading.m1()
#methodOverloading.m1(10)
methodOverloading.m1(10,20)