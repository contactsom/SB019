# Defination of the Function

def getMyGreetings(name,message):
    greetings=name+" "+message
    return greetings


output=getMyGreetings("How are you","Shezan")
print(output)

output1=getMyGreetings(name="Shezan",message="How are you")
print(output1)

output2=getMyGreetings(message="How are you",name="Shezan")
print(output2)