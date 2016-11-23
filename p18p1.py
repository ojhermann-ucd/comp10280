"""
Pseudocode
Using the makeLower function from the slides to establish the appropriate input of an all lower case letter string

if length of input is 0 or 1, return true

if lenght of input larger than 1:
	starting from the outermost elements, compare; if they match, continue to the next two outer most; etc
	if fail return false
	if complete, return true


"""
#from the slides/p17p5.py
def makeLower(s):
	output = ""
	s = s.lower()
	for c in s:
		if c in "abcdefghijklmnopqrstuvwxyz":
			output += c
		else:
			pass
	return output

#modified isPal
def isPal(s):
	if len(s) == 0 or len(s) == 1:
		return True
	else:
		for i in range(0, (len(s) // 2) + 1, 1):
			if s[i] == s[-i - 1]:
				pass
			else:
				return False
		return True

stringInput = input("Please enter a string: ")
if isPal(makeLower(stringInput)):
	print(stringInput, "is a palindrome.")
else:
	print(stringInput, "is not a palindrome.")
print("")
print("Note: the underlying algorithm is an interable version of the recursive function in the slides, so any peculiarities or failings of the algorithm are not a fault, but part of what I was asked to do.")