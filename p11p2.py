"""
Write a program that prompts the user for an integer and uses a while loop to calculate that number of terms of the Fibonacci Series.
Try to make the program as small and efficient as possible.
Save this program as p11p2.py.

Pseudocode

"""
import sys

while True:
     try:
          num = int(input("Enter a positive integer value, please: "))
          break
     except ValueError:
          print("Restart the program and enter a positive integer value if you wish to continue.")
          sys.exit()
          break

fib1 = 0
fib2 = 1
fibn = 0
count = 1
if num < 1:
	print("Restart the program and enter an integer greater than 0 if you wish to continue.  Notice that fib(1) = 0 and fib(2) = 1.")
else:
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