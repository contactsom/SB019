'''
Palindrom a String
Input : MADAM
Output : MADAM
'''

mystring = "MADAM"
if(mystring==mystring[::-1]):
    print(mystring,"Is Palindrom")
else:
    print(mystring, "Is NOT Palindrom")