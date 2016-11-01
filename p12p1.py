"""
Write a function that takes as its single argument a non-negative integer and returns the factorial of the number.

Write a program that prompts the user for an integer and checks that the number entered is non-negative.
If it is, it calls the function defined in part (a) and prints out the result; if not, it prints out an appropriate error message.

Pseudocode
def fac(number):
	if number = 0:
		return 1
	else:
		return number * fac(number - 1)

make user enter an iteger value
check if integer value is positive
call the program
"""
import sys

def fact(n):
	output = 1
	while n > 0:
		output *= n
		n -= 1
	return output

while True:
	try:
		num = int(input("Enter an integer value, please: "))
		break
	except ValueError:
		print("Restart the program and enter an integer value if you wish to continue.")
		sys.exit()

if num < 0:
	print("You entered a negative integer and the factorial function is only defined on positive integers.")
else:
	print(str(num) + "! = " + str(fact(num)))