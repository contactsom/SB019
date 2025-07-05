def devideNumber(a,b):
    c=0
    try:
        c=a/b
    except:
        print("Invalid Denominator")
    return c


output1=devideNumber(10,20)
print(output1)

output2=devideNumber(10,2)
print(output2)

output3=devideNumber(10,0)
print(output3)