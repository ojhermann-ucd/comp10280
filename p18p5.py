"""
Pseudocode

take user input

count each occurance of "xyz"
count each occurance of ".xyz"
take the difference

print the results
"""

stringInput = input("Please enter what you would like: ")

def xyzCheck(s):
	xyzCount= 0
	xyzCount += s.count("xyz")
	xyzCount -= s.count(".xyz")
	return xyzCount

print("There are ", xyzCheck(stringInput), "occurances.")