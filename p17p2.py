"""
Pseudocode
codes used from p17p1 explained in p17p1

two integers m and n:
	if m or n is zero:
		return zero
	else:
		return all elements of all Divs(m) that are in allDivs(n)
"""

import sys

def posDivs(n):
	nRange = range(2, (n // 2) + 1, 1)
	if n == 0:
		return "Every number is a divisor of zero."
	else:
		output = [i for i in nRange if n % i == 0]
		output.extend([1, n])
		output = list(set(output))
		output.sort()
		return output

def negDivs(n):
	if n == 0:
		return "Every number is a divisor of zero."
	elif n < 0:
		m = -n
		output = [-i for i in posDivs(m)]
	else:
		output = [-i for i in posDivs(n)]
	return output

def allDivs(n):
	if n == 0:
		return "all the integers; every number is a divisor of zero."
	else:
		n = abs(n)
		output = posDivs(n)
		output.extend(negDivs(n))
		output = list(set(output))
		output.sort()
		return output

def cdivs(m, n):
	if m == 0 or n == 0:
		return [0]
	else:
		output = [i for i in allDivs(m) if i in allDivs(n)]
		return output

while True:
	try:
		num1 = int(input("Please enter the first integer (or a non-integer to exit): "))
		num2 = int(input("Please enter the second positive integer (or a non-integer to exit): "))
		print("The common divisors of", str(num1), "and", str(num2), "are", str(cdivs(num1, num2)))
		print("Remember, if x = y * z, then x = -y * -z")
		print("")
	except ValueError:
		print("Thank, you.  Goodbye.")
		sys.exit()