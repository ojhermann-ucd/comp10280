"""
Pseudocode

Request user input

define the case senitive string I want to count

count the number of occurances of the string in the input

"""

stringInput = input("Please enter what you would like: ")

def stringInputCount(s):
	return s.count("code")

print(stringInputCount(stringInput))