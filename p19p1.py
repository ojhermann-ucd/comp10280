#question: if n < b, do we need to write code to present integers < b in some unique form?
#no according to JD

"""
Pseudocode
input number and base
divide number by base
- remainder is least significant digit of base representation of number
- number is now quotient
repeteat until number is zero

"""

import sys

def newBaseRep(n, b):
	newRep = []
	while n > 0:
		q = n // b
		r = n % b
		newRep.insert(0, r)
		n = q
	output = ""
	for i in newRep:
		output += str(i)
	return int(output)

while True:
	try:
		#base 10 input
		numBase10 = input("Please enter a positive integer in base 10 (or q to exit): ")
		if numBase10 == "q":
			print("Goodbye!")
			sys.exit()
		elif int(numBase10) < 0:
			print("You did not enter a positive integer.")
		else:
			numBase10 = int(numBase10)
		
		#new base input
		newBase = input("Please enter a positive integer greater than 1 for a new base (or q to exit): ")
		if newBase == "q":
			print("Goodbye!")
			sys.exit()
		elif int(newBase) < 1:
			print("You did not enter a positive integer greater than 1.")
		else:
			newBase = int(newBase)
		
		#function
		print(newBaseRep(numBase10, newBase))
		print("if the base ten number was less than the new base, the original base ten representation has been returned")
		print("confirmed by Professor Dunnion on 24 Nov 2016")
	
	except ValueError:
		print("Please reread the instructions and try again.")
