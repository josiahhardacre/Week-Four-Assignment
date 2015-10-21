# Josiah Hardacre Collaborated with Nicole Ignasiak, Nathan Pugh, and Trevor Waite
# CIS 125 82A
# 9/30/15
# Week 4 Lab

# Open the file *getty.txt* for reading.  
gettyfile = open("getty.txt", "r")
# Open a new file *piggy.txt* for writing.  
piggyfile = open("piggy.txt", "w")
# Read the getty.txt file into a string.  
address = gettyfile.read()
# Strip out bad characters (, - .).  
address = address.replace(".","")
address = address.replace(",","")
address = address.replace("-","")

def piggy():
# Split the string into a list of words.  
	listaddress = address.split()
# Create a new empty string.  
	piggystring = ""
  
	vowels = "aeiouAEIOU"     
	piggynewword = ""

#Loops through every word in the Gettysburg Address
	for word in listaddress:
		if word[0] in vowels:
			piggynewword = word + "yay"
			piggystring = piggystring + " " + piggynewword
		else:
			n=0
# Finds the first vowel and then changes word to PigLatin			
			for letter in word:
				if letter in vowels:
# Add the pigified word (and a space) to the new string.
					piggynewword = (word[n:] + word[0:n] + "ay")
					piggystring = piggystring + " " + piggynewword
					break
				n+=1
	return piggystring
			
# Calls the function piggy()
finalpiggystring = piggy()
# Write the new string to piggy.txt.  
piggyfile.write(finalpiggystring)
# close the files.
piggyfile.close()
gettyfile.close()