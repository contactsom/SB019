# Function Aliasing

def wish(name):
    print("Good Morning :",name)



greetings=wish # Aliasing

del wish
wish("Pankaj")  # NameError: name 'wish' is not defined

greetings("Pankaj")

print(id(wish))
print(id(greetings))