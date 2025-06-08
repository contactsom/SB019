# String Slicing
# [m:n]
# Where m : Start Index or FROM
# Where n : End Index or TO
# [FROM : TO]
# TO=(n-1)
# Example [1:5] = [1:5-1]

# -8 -7 -6 -5 -4 -3 -2 -1 -> -Ve Index
#  A  B  C  D  E  F  G  H
#  0  1  2  3  4  5  6  7 -> +Ve Index

myString="ABCDEFGH"

print("[1:5]",myString[1:5]) #BCDE
print("[1:7]",myString[1:7]) #BCDEFG
print("[1:7]",myString[4:7]) #EFG
print("[0:0]",myString[0:0]) #
print("[0:7]",myString[0:7]) #ABCDEFG
print("[0:8]",myString[0:8]) #ABCDEFGH
print("[0:80]",myString[0:80]) #ABCDEFGH
print("[:80]",myString[:80]) #ABCDEFGH
print("[0:]",myString[0:]) #ABCDEFGH
print("[:]",myString[:]) #ABCDEFGH






