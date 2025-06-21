# Function Aliasing

def wish(name):
    print("Good Morning :",name)

wish("Pankaj")

greetings=wish # Aliasing
greetings("Pankaj")

print(id(wish))
print(id(greetings))