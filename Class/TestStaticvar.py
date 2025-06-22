class TestStaticvar:
    x=10 # Static Variable

    def __init__(self):
        self.y=20


testStaticvar1=TestStaticvar()
testStaticvar2=TestStaticvar()

print("************BEFORE********************")
print("testStaticvar1 Value of X :: ",testStaticvar1.x)
print("testStaticvar1 Value of Y :: ",testStaticvar1.y)

print("********************************")

print("testStaticvar2 Value of X :: ",testStaticvar2.x)
print("testStaticvar2 Value of Y :: ",testStaticvar2.y)

print("***********AFTER*********************")
TestStaticvar.x=888 # Calling the static Variable using Class Name
testStaticvar1.y=999 # Instance /non-static variable you can call using object only.

print("testStaticvar1 Value of X :: ",testStaticvar1.x)
print("testStaticvar1 Value of Y :: ",testStaticvar1.y)

print("********************************")
print("testStaticvar2 Value of X :: ",testStaticvar2.x)
print("testStaticvar2 Value of Y :: ",testStaticvar2.y)