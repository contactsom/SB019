'''
Check if Two String are Anagrams
Defination : Both the string have same characters with same frequency. So, they are anagrams.
Input : "listen"
Output : Silent
'''

s1 = "listen"
s2 = "silent"

if (sorted(s1)==sorted(s2)):
    print("Anagrams")
else:
    print("NOT Anagrams")