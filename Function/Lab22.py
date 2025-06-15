# Defination of the Function

def getMyGreetings(name="Raj",msg="Good Morning !!!"):
    greet="Hello-"+name+" "+msg
    return greet


output=getMyGreetings("Sripriya")
print(output)

output1=getMyGreetings()
print(output1)

output3=getMyGreetings("Sripriya","Good Evening !!!")
print(output3)