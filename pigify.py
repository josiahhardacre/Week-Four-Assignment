# 
# File Header
#
# Define vowels

vowels = "aeiouAEIOU"         #I solved the case sensitivity by adding the vowels in both lowercase and uppercase.

# Ask for word

word = input("Please enter a word: ")

if (originalword[0] in vowels):
    print((originalword + endofvowel).capitalize())
    
else:
    print((originalword[1:] + originalword[0] + endofconsonant).capitalize())
# Loop through word, one letter at a time

for letter in word:
	if letter in vowels:
		pig = word + "yay"
	else:
		# False? Consonant
		pig = word[1:] + word[0] + "ay"


print(pig)

