
#   0,  1,  2,  3,  4,  5
# [ 10, 20, 30, 40, 50, 60]
#   -6, -5, -4, -3, -2, -1

nameList=[10,20,30,40,50,60]
print("[1:3]",nameList[1:3])
print("[2:3]",nameList[2:3])
print("[0:3]",nameList[0:3])
print("[0:5:2]",nameList[0:5:2]) # 10,  30, 50

# First Index < last Index
# -1 > -3 = False
print("[-1:-3]",nameList[-1:-3]) # []
print("[-3:-1]",nameList[-3:-1]) #
print("[-6:-6]",nameList[-6:-6]) #
print("[-5:-1:2]",nameList[-5:-1:2]) # [20, 40]
print("[-5:-1:-1]",nameList[-5:-1:-1]) #
