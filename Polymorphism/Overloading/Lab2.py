class Lab1:
    def sum(self,*a):
        sum=0
        for x in a:
            sum=sum+x
        print("SUM ::",sum)


obj1=Lab1()
obj1.sum(10,20)
obj1.sum(10,20,30)
obj1.sum()