"""
Pseudocode

define variables, including user input string

count occurances of strings in the user input string

if the occurances are the same, print message; otherwise, print other message
"""


var1 = "cat"
var2 = "dog"
inputString = input("Please enter a string of whatever you would like: ")

if inputString.count(var1) == inputString.count(var2):
	print(str(var1), "occurs", str(inputString.count(var1)), "and", str(var1), "occurs", str(inputString.count(var2)), ", so they both occur the same number of times.")
else:
	print(str(var1), "occurs", str(inputString.count(var1)), "and", str(var1), "occurs", str(inputString.count(var2)), ", so they do not occur the same number of times.")