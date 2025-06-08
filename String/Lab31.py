# String Slicing
# [m:n:i]
# Where m : Start Index or FROM
# Where n : End Index or TO
# Where i : is Called Interval
# [FROM : TO]
# TO=(n-1)
# Example [1:5] = [1:5-1]

# -8 -7 -6 -5 -4 -3 -2 -1 -> -Ve Index
#  A  B  C  D  E  F  G  H
#  0  1  2  3  4  5  6  7 -> +Ve Index

myString="ABCDEFGH"

print("[0:5:1]",myString[0:5:1]) #ABCDE
print("[0:5:2]",myString[0:5:2]) #ACE
#print("[0:5:0]",myString[0:5:0]) #ValueError: slice step cannot be zero
print("[0:7:3]",myString[0:7:3]) #ADG






