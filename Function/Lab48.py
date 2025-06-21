# Nested Function

def outer():
    print("I am outer ")
    def inner():
        print("I am Inner ")
    print("Outer Function is cllling Inner Function")
    inner()


outer()