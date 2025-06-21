# Function Aliasing

def wish(name):
    print("Good Morning :",name)



greetings=wish # Aliasing

del greetings
wish("Pankaj")
greetings("Pankaj") # NameError: name 'greetings' is not defined

print(id(wish))
print(id(greetings))