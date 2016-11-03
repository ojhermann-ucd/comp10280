"""
(a) Write a recursive function that takes as its single argument a non-negative integer and returns the factorial of the number.
(b) Write a program that prompts the user for an integer and checks that the number entered is non-negative. If it is, it calls the function defined in part (a) and prints out the result; if not, it prints out an appropriate error message.
(c) In your function, include some print statements that allow you to see the operation of the recursion and its progress towards the base case.
Save this program as p13p6.py.

Pseudocode
recursively define fac(n)
fac(n):
if n == 0:
	return 1
else:
	return n * fac(n - 1)

user enters apprpriate non-neg int; otherwise exit program with message

printed commentary on the function has been included

"""

import sys

def factorial(n):
	"""
	Recursively defined factorial

	Assumptions
	- n is a non-negative integer
	"""
	if n == 0:
		print(str(n) + "! = 1 "+ " is the last multiplicand")#print requirement for (c)
		return 1
	else:
		print(str(n) + " is a multiplicand")#print requirement for (c)
		return n * factorial(n - 1)

#prompt user for the number
while True:
	try:
		num = int(input("Enter a non-negative integer value: "))
		break
	except ValueError:
		print("Restart the program and enter a non-negative integer value if you wish to continue.")
		sys.exit()

#run the program
if num < 0:
	print("Restart the program and enter a non-negative integer value if you wish to continue.")
else:
	print(factorial(num))