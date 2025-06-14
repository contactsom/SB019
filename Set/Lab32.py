# Write a Program to print the Vowel from the given Word

word=input("Enter the word to search for vowel :: ")
mySet=set(word)
vowel={'a','e','i','o','u'}

mywordVowel=mySet.intersection(vowel)

print(mywordVowel)