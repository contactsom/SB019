# Nested List

nameList=[[10,20,30],[40,50,60],[11,10,30]]
print(type(nameList))

for sublist in nameList:
    for item in sublist:
        print(item)
