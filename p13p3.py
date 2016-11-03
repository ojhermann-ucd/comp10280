"""
Implement the program that uses the print max function from today’s lectures (Page 9 of the notes).
Ensure that you understand what is going on and how it works. Save this program as p13p3.py.

Program to print out the largest of two numbers entered by the user
Uses two functions:  max and print_max

Pseudocode
- place p13p2.py inside of another function (you have access to this for its pseudocode)
- include user input requests within this function
- print the results of the inputs in the max_example function

Error Checking Notes

"""
import sys

def print_max_example():
	"""
	function: prints the result of max_example
	"""
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
	#print stuff
	print("The largest of " + str(numA) + " and " + str(numB) + " is " + str(max_example(numA, numB)))
	#gratuitous return
	return

print_max_example()