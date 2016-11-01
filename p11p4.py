"""
Write a program that prompts the user for an integer and calculates that number of Catalan Numbers.
Save this program as p11p4.py.

Pseudocode
have user input an integer
if negative, exit and give message
if positive:
	calculat the numerator
	calculate first half of denominator
	calculate second half of denominator
	divide numerator by product of denominator halves
	print each Catalan number up to the integer (starting from 0)
"""
import sys

while True:
	try:
		num = int(input("Enter a positive integer value n to see the Catalan numbers for 0 to n: "))
		break
	except ValueError:
		print("Restart the program and enter a positive integer value if you wish to continue.")
		sys.exit()

if num < 0:
	print("Restart the program and enter a non-negative integer value if you wish to continue.")
else:
	if num == 0:
		catNum = int(1)
		print("Catalan Number for n = " + str(num) + " is " + str(catNum))
	else:
		catRange = range(0, num + 1, 1)
		for c in catRange:
			numerator = 1
			if c == 0:
				numerator = 1
			else:
				for n in range(1, (2 * c) + 1, 1):
					numerator *= n
			denom2 = 1
			if c == 0:
				denom2 = 1
			else:
				for n in range(1, c + 1, 1):
					denom2 *= n
			denom1 = denom2 * (c + 1)
			catNum = int(numerator / (denom1 * denom2))
			print("Catalan Number for n = " + str(c) + " is " + str(catNum))