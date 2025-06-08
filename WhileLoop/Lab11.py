
# In the String "SIMPLILEARN" if I found the 'R' then say "R" found
myEdtech="SIMPLILEARN"
#myEdtech="SIMPLILEAXN"
length=len(myEdtech)

i=0
while(i<length):
    if(myEdtech[i]=='L'):
        print("L Found at ",i," Index")
    else:
        print("L Not Found")
    i=i+1