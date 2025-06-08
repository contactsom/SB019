# For Loop with Else Condition and Break

myNumber=[8,90,1,2,3,4,5,6]

i=0
for n in myNumber:
    if (n==4):
        print(n," Found at index : ",i) # 5
        break
    i=i+1
else:
    print("For Loop Completed Successfully")
    