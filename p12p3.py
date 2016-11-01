"""
Write a function that takes as its two arguments a number and a tolerance and, 
using the technique exposed in lectures, returns an approximation of the square root of the number that is within the tolerance.

Write a program that prompts the user for a floating-point number and checks that the number entered is non-negative. 
If it is, it calls the function defined in part (a) with the number and a tolerance defined in the program and prints out the square root of the number; 
if not, it prints out an appropriate error message.

Pseudocode
def sroot(n, e):
	function will, using user input number n and margin of error e check that difference of n and an assumed root (starting at zero) are within e
	if not within e, increment root by e^2
	continue this process until either an acceptable approximation is found or root^2 is larger than n
	print according message

"""
import sys

def sroot(num, epsilon):
	step = epsilon ** 2
	root = 0
	numGuesses = 0
	while epsilon <= abs(num - root**2) and root**2 <= num:
		root += step
		numGuesses += 1
		if numGuesses % 100000 == 0:
			print("Still running. Number of guesses: " + str(numGuesses))
		else:
			pass
	print("Number of guesses: " + str(numGuesses))
	if abs(num - root**2) < epsilon:
		print("The approximate square root of " + str(num) + " is " + str(root))
	else:
		print("Failed to find a square root of " + str(num))
	print("Finished!")

while True:
	try:
		num = float(input("Enter a floating point value that you would like to know the square root of: "))
		if num < 0:
			print("Restart the program and enter a positive floating point value if you wish to continue.")
			sys.exit()
		break
	except ValueError:
		print("Restart the program and enter a floating point value if you wish to continue.")
		sys.exit()

while True:
	try:
		tol = float(input("Enter a floating point value that you would like to use as your tolerance margin: "))
		if tol < 0:
			print("Restart the program and enter a positive floating point value if you wish to continue.")
			sys.exit()
		elif tol == 0:
			print("We're using floating point numbers, so you cannot have 0 margin of error.  Please start over again.")
			sys.exit()
		break
	except ValueError:
		print("Restart the program and enter a floating point value if you wish to continue.")
		sys.exit()

sroot(num, tol)