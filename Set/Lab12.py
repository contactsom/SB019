
myAlphabetSet={10,20,30,40,50,10,50}

print("********Before Add***********")
for data in myAlphabetSet:
    print(data)

print("*********After Add**********")
myAlphabetSet.add(500)
for data in myAlphabetSet:
    print(data)