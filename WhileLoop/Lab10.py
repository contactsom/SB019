
# In the String "SIMPLILEARNR" if I found the First 'R' then say "R" found
myEdtech="SIMPLILEARNR"
length=len(myEdtech)

i=0
while(i<length):
    if(myEdtech[i]=='R'):
        print("R Found")
        break

    i=i+1