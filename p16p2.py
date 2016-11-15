"""
Pseudocode
make sure inputs are positive integers as requested

define function that determines codivisors for two inputs:
- for numbers in range from 1 up to the smaller of two inputs, if both inputs are divisible by such number, add such number to list
- return list

define a function that sums the output of the previous function

print both the codivisors and the sums

"""


import sys

def cdivs(m, n):
	divsRange = range(1, min(n + 1, m + 1), 1)
	output = [i for i in divsRange if m % i == 0 and n % i == 0]
	return output

def sumCdivs(m, n):
	return sum(cdivs(m, n))

while True:
	try:
		num1 = int(input("Please enter the first positive integer (or a non-integer to exit): "))
		if num1 < 0:
			print("Thank, you.  Goodbye.")
			sys.exit()
		else:
			num2 = int(input("Please enter the second positive integer (or a non-integer to exit): "))
			if num2 < 0:
				print("Thank, you.  Goodbye.")
				sys.exit()
		print(cdivs(num1, num2), " is the list of common divisors, which sums to ", sumCdivs(num1, num2))
		print("")
	except ValueError:
		print("Thank, you.  Goodbye.")
		sys.exit()