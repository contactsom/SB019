# String Slicing
# [m:n:i]
# Where m : Start Index or FROM
# Where n : End Index or TO
# Where i : is Called Interval
# [FROM : TO]
# TO=(n-1)
# Example [1:5] = [1:5-1]
# Start Index will be lesser than End Index i.e FROM<TO

# -8 -7 -6 -5 -4 -3 -2 -1 -> -Ve Index
#  A  B  C  D  E  F  G  H
#  0  1  2  3  4  5  6  7 -> +Ve Index

myString="ABCDEFGH"

print("[-0:-0]",myString[-0:-0]) # No Output
print("[-1:-0]",myString[-1:-0]) # No Output
print("[-1:-1]",myString[-1:-1]) # No Output
print("[-1:-4]",myString[-1:-4]) # No Output # -1<-4=False

print("[-8:-2]",myString[-8:-2]) #ABCDEF
print("[-6:-1]",myString[-6:-1]) #CDEFG







