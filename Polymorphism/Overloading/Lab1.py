class Lab1:
    def sum(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            print("Sum of A+B+C :: ",a+b+c)
        elif (a!=None and b!=None):
            print("Sum of A+B :: ", a + b )
        else:
            print("Please provide the at least two or Three value to get the Sum ")


obj1=Lab1()
obj1.sum(10,20)
obj1.sum(10,20,30)
obj1.sum()