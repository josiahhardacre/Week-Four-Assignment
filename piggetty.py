# Josiah Hardacre Collaborated with Nicole Ignasiak, Nathan Pugh, and Trevor Waite
# CIS 125 82A
# 9/30/15
# Week 4 Lab

# Define a function called piggy(string) that returns a string

def piggy(word):
	
	# Magic Happens Here
	pig = word
	# Ignore previous line
	
	return pig

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

print (address)
# Split the string into a list of words.  
listaddress = address.split()
# Create a new empty string.  
piggystring = ""
# Loop through the list of words, pigifying each one.  
vowels = "aeiouAEIOU"     
piggynewword = ""

#Loops through every word in the Gettysburg Address
for word in listaddress:
	if word[0] in vowels:
		piggynewword = word + "yay"
		piggystring = piggystring + " " + piggynewword
	else:
		n=0
		for letter in word:
			if letter in vowels:
# Add the pigified word (and a space) to the new string.
				piggynewword = (word[n:] + word[0:n] + "ay")
				piggystring = piggystring + " " + piggynewword
				break
			n=1
# Write the new string to piggy.txt.  
piggyfile.write(piggystring)
# close the files.
piggyfile.close()
gettyfile.close()