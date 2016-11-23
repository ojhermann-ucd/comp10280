"""
Pseudocode

Request user input

define the case senitive string I want to count

count the number of occurances of the string in the input

"""

stringInput = input("Please enter what you would like: ")

def checkFunny(s):
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	copeCount = 0
	for i in alphabet:
		copeValue = "co" + i + "e"
		copeCount += s.count(copeValue)
	return copeCount

print("There are ", checkFunny(stringInput), "occurances.")