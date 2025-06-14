# Nested List

nameList=[10,20,30,[40,50,60],7,3,9,[11,10,30],50,60]
print(type(nameList))

for items in nameList:
    if isinstance(items,list): # is items which I recived from nameList is a "List" or Not
        for item in items:
            print(item)
    else:
        print(items) # Print the Single Element