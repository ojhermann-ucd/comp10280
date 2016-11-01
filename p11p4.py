"""
Write a program that prompts the user for an integer and calculates that number of Catalan Numbers.
Save this program as p11p4.py.

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

catRange = range(0, num, 1)
for c in catRange:

	numerator = 1
	for n in range(1, (2 * c) + 1, 1):
		numerator *= n

	denom2 = 1
	for n in range(1, c + 1, 1):
		denom2 *= n

	denom1 = denom2 * (c + 1)

	catNum = int(numerator / (denom1 * denom2))

	print("Catalan Number for n = " + str(c) + " is " + str(catNum))