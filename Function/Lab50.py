# Function Decorators

def decor(func):
    def inner(name):
        if name=="Pranay":
            print("Hello Pranay Are you Slipping")
        else:
            func(name)
    return inner


@decor
def wish(name):
    print("Hello",name," Good Morning")

wish("Pranay")
wish("Florance")
wish("Kashish")