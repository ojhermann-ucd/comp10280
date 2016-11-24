"""
Pseudocode

use each digit in the input number as a weight to multiply an appropriate power of the given base
lest significant digit has power of 0, with each power incrementing by one
"""

import sys

def toBaseTen(n, b):
	baseTen = 0
	count = 0
	for i in reversed(n): #use of reversed OK by Khalil on 23 Nov 2016
		baseTen += int(i) * (int(b) ** count)
		count += 1
	return baseTen

while True:
	try:
		#base 10 input
		numInput = input("Please enter a digits representing some number in a given base (or q to exit): ")
		if numInput == "q":
			print("Goodbye!")
			sys.exit()
		elif int(numInput) < 0:
			print("You did not enter a positive integer.")
		else:
			numInput = numInput
		
		#new base input
		theBase = input("Please enter a positive integer greater than 1 as the base of the number just entered (or q to exit): ")
		if theBase == "q":
			print("Goodbye!")
			sys.exit()
		elif int(theBase) < 1:
			print("You did not enter a positive integer greater than 1.")
		else:
			theBase = theBase
		
		#function
		print(toBaseTen(numInput, theBase))
		print("Note: I was told the only inputs would be integers e.g. no f6 for a hexidecimal number or g7 for a base 17 number.")
		print("Note: Professor Dunnion confirmed that we are not being asked to also create a procedure for generating a numeral system for an arbitrary base.")
		print("Note: this limits what can be entered, but this program would work if we had been expected to produce a more general input system.")
	except ValueError:
		print("Please reread the instructions and try again.")