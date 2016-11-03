"""
Implement the programs that illustrate the definition and use of functions in Python from today’s lectures (Pages 4 and 5 of the notes).
Save these programs as p13p1.py and p13p2.py, respectively.


Program to print out the largest of two numbers entered by the user
Uses a function max
Uses max in a print statement


Pseudocode
define function:
	return greater of two numbers

have user input floating numbesr; exit with message otherwise

print messages using function in the print statement

Error Checking

"""
import sys

def max_example(a, b):
	"""
	function: returns the maximum of two numbers

	assumptions:
	- a is a non-negative integer
	- b is a non-negative integer
	"""
	if a > b:
		return a
	else:
		return b

#prompt user for the first number
while True:
	try:
		numA = float(input("Enter a floating point value: "))
		break
	except ValueError:
		print("Restart the program and enter a floating point value if you wish to continue.")
		sys.exit()

#prompt user for the second number
while True:
	try:
		numB = float(input("Enter a floating point value: "))
		break
	except ValueError:
		print("Restart the program and enter a floating point value if you wish to continue.")
		sys.exit()

#print things
print("The largest of " + str(numA) + " and " + str(numB) + " is " + str(max_example(numA, numB)))
print("Finished!")