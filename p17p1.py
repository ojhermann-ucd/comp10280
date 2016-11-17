"""
Pseudocode

positive divisors:
output = [1, n]
divide n by all numbers in range(2, n//2 + 1, 1):
	if divisible, add divisor to list

negative divisors:
add mulitple of each element of positive list by -1 and add that to list

if n = 0 print message that all numbers are divisors of zero.
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

while True:
	try:
		num = int(input("Please enter an integer (or something else to exit): "))
		print("The divisors of", str(num), "are", str(allDivs(num)))
		print("Remember, if x = y * z, then x = -y * -z")
		print("")
	except ValueError:
		print("Thank, you.  Goodbye.")
		sys.exit()