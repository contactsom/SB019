
myAlphabetSet={'A','B','C','D','E'}
length=len(myAlphabetSet)
print(length)

i=0
while i<length:
    print(myAlphabetSet[i]) # TypeError: 'set' object is not subscriptable
    i=i+1

    # myAlphabetSet[0]
    # myAlphabetSet[1]
    # myAlphabetSet[2]