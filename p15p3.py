"""
Pseudocode

define a recursive function to calculat each element of the sequence
define a function that uses the function on each value of a given number from 1 up to that number
"""

import sys

#underlying recursive function
def fnc(n):
	if n == 0:
		return 13
	elif n == 1:
		return 8
	else:
		return fnc(n - 2) + 13 * fnc(n - 1)

#function to display each element of the recursion
def fncSeq(p):
	for i in range(0, p + 1, 1):
		if i == 0 or i == 1:
			print("fnc(" + str(i) + ") = " + str(fnc(i)) + " by definition")
		else:
			print("fnc(" + str(i) + ") = " + str(fnc(i)) + " = " + "fnc(" + str(i - 2) + ") + 13 x f(" + str(i - 1) + ")")
	return "I would have used @functools.lru_cache(None) to make this quick, but I assuem that is off limits in this course"

while True:
	try:
		num = int(input("Please enter an integer greater than 1 (or a negative integer to exit): "))
		if -1 < num:
			print(fncSeq(num))
		else:
			print("Thank you, goodbye.")
			sys.exit()
	except ValueError:
		print("You must enter an integer greater than 0.")
		sys.exit()