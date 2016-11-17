"""
Pseudocode for the actual code is in the slides we were told to take it from; see p17p5.py for a focus on using Professor Dunnion's algorithm

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
print("")
print("first we decompose", stringInput, "into only the lowercase letter elements, which is", makeLowerChar(stringInput))
print("")
print("then we start comparing the outermost pairs of letters, seeing if they match; if they all do, then we have a palindrome.")
print("")

#print through the outermost layers of the modified string, mimicing the recursive steps
rangeObject = makeLowerChar(stringInput)
rangeLength = len(rangeObject)
if rangeLength == 0 or rangeLength == 1:
	print("Any string of length zero or one is a palindrome.")
else:
	for i in range(0, (rangeLength // 2) + 1, 1):
		if rangeObject[i] == rangeObject[-i - 1]:
			print(rangeObject[i], "=", rangeObject[-i - 1])
		else:
			print(rangeObject[i], "!=", rangeObject[-i - 1])
			break

print("")
if isPal(makeLowerChar(stringInput)):
	print(stringInput, "is a palindrome.")
else:
	print(stringInput, "is not a palindrome.")

print("")
print("Note: the underlying algorith is directly transcribed from the slides, so any peculiarities or failings of the algorithm are not a fault, but part of what I was asked to do.")