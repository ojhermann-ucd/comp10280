"""
Write a program that prompts the user for a series of integers and, for each of the numbers entered, uses a for loop to calculate that number of terms of the Fibonacci Series. 
The program should stop when a negative number is entered.
Save this program as p11p3.py.

Pseudocode
user inputs integer
if integer is negative, message and exit
if integer is positive:
	fibRange = 0 to integer + 1
	for f in fibRange:
	     if f = zero, print fib(0)
	     if f = 1, print fib(1)
	     else:
	     	fibn = fib1 + fib 2
	     	fib1, fib2 = fib2, fibn
	     	print(fib(n))
"""
import sys

while True:
	try:
		num = int(input("Enter a positive integer value greater than 0, please (enter a negative integer to exit the program): "))
		fib1 = 0
		fib2 = 1
		fibn = 0
		fibRange = range(1, num + 1, 1)
		if num < 0:
			print("You have entered a negative integer and the program has ended.")
			sys.exit()
		elif num == 0:
			print("If you wish to continue using this program, please enter an integer greater than 0.  To quit, enter a negative integer.")
		else:
			for i in fibRange:
				if i == 1:
					print("fib(" + str(i) + ") = " + str(fib1))
				elif i == 2:
					print("fib(" + str(i) + ") = " + str(fib2))
				else:
					fibn = fib1 + fib2
					fib1, fib2 = fib2, fibn
					print("fib(" + str(i) + ") = " + str(fibn))
	except ValueError:
		print("Restart the program and enter a positive integer value if you wish to continue.")
		sys.exit()