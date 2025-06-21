# Generator Function


def getcounter(num):
    print("Start Contdown")
    while(num>0):
        yield num
        num=num-1

values=getcounter(5)

for x in values:
    print(x)
