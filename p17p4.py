"""
Pseudocode for this is in the slides we were told to take it from.

Note: this is directly transcribed, so any pecadillos for the algorithm are not a fault, but part of what I was asked to do.
"""

#from the slides
def makeLowerChar(s):
	output = ""
	s = s.lower()
	for c in s:
		if c in "abcdefghijklmnopqrstuvwxyz":
			output += c
		else:
			pass
	return output

#also from slides
def isPal(s):
	if len(s) <= 0:
		return True
	else:
		return s[0] == s[-1] and isPal(s[1:-1])

stringInput = input("Please enter a string: ")
if isPal(makeLowerChar(stringInput)):
	print(stringInput, "is a palindrome.")
else:
	print(stringInput, "is not a palindrome.")
print("Note: this is directly transcribed from the slides, so any peculiarities or failings of the algorithm are not a fault, but part of what I was asked to do.")