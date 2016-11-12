"""
Pseudocode

define a recursive function to calculat each element of the sequence
define a function that uses the function on each value of a given number from 1 up to that number
"""

import sys

#underlying recursive function
def fnc(n):
	if n == 1:
		return 2
	else:
		return n + fnc(n - 1)


#function to display each element of the recursion
def fncSeq(p):
	for i in range(1, p + 1, 1):
		if i == 1:
			print("fnc(" + str(i) + ") = " + str(fnc(i)) + " by definition")
		else:
			print("fnc(" + str(i) + ") = " + str(fnc(i)) + " = " + str(i) + " + " + str(fnc(i) - i) + " = " + str(i) + " + " + "fnc(" + str(i - 1) + ")")
	return "I would have used @functools.lru_cache(None) to make this quick, but I assuem that is off limits in this course"

while True:
	try:
		num = int(input("Please enter an integer greater than 1 (or a negative integer to exit): "))
		if 0 < num:
			print(fncSeq(num))
		else:
			print("Thank you, goodbye.")
			sys.exit()
	except ValueError:
		print("You must enter an integer greater than 0.")
		sys.exit()