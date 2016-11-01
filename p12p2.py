"""
Write a function that takes as its argument a non-negative integer and prints out that number of terms of the Fibonacci Series (you may assume that the first term is the 0th term). 
This function should not return an explicit value.

Write a program that prompts the user for an integer and checks that the number entered is non-negative. 
If it is, it calls the function defined in part (a); if not, it prints out an appropriate error message.

Pseudocode
def fib(n):
	while count < num + 1:
	if n = 0:
		print(1)
	elif n = 1:
		print(1)
	else:
		fib_n = fib1 + fib2
		fib1, fib2 = fib2, fibn
		print(fibn)
	count += 1

user enters integer
if integer negative:
	tell them to restart and try again
else:
	call fib(integer)

"""
import sys

def fib(num):
	fib1 = 0
	fib2 = 1
	fibn = 0
	count = 1
	while count < num + 1:
		if count == 1:
			print("fib(" + str(count) + ") = " + str(fib1))
		elif count == 2:
			print("fib(" + str(count) + ") = " + str(fib2))
		else:
			fibn = fib1 + fib2
			fib1, fib2 = fib2, fibn
			print("fib(" + str(count) + ") = " + str(fibn))
		count += 1

while True:
	try:
		num = int(input("Enter a non-zero positive integer value to see the fib numbers up to that integer e.g. fib(1) = 0, fib(2) = 1, fib(3) = fib(1) + fib(2): "))
		break
	except ValueError:
		print("Restart the program and enter an appropriate integer value if you wish to continue.")
		sys.exit()

if num < 1:
	print("Restart the program and enter an appropriate positive integer value if you wish to continue.")
else:
	fib(num)