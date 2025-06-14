'''
Count Vowel and Consonent in a String
Input : MADAM
Output : MADAM
'''

mystring = "MADAM"
vowel="AEIOUaeiou"

vowelCount=sum(1 for count in mystring if count in vowel )
print("Number of Vowel ::",vowelCount)

consonentCount=sum(1 for count in mystring if count not in vowel )
print("Number of Consonent ::",consonentCount)
