"""
Pseudocode
ensure that input meets criteria

recursively define the function

define function that prints each value from 1 up to input using the recursively defined function

"""

import sys

def fnc(n):
	if n == 1:
		return 2
	else:
		return 2 * fnc(n - 1)

def fncSeq(p):
	for i in range(1, p + 1, 1):
		if i == 1:
			print("fnc(" + str(i) + ") = " + str(fnc(i)) + " by definition")
		else:
			print("fnc(" + str(i) + ") = " + str(fnc(i)) + " = 2 x " + "fnc(" + str(i - 1) + ")")
	return "I would have used @functools.lru_cache(None) to make this quick, but I assume that is off limits in this course"

while True:
	try:
		num = int(input("Please enter an integer greater than 0 (or an integer < 1 to exit): "))
		if 0 < num:
			print(fncSeq(num))
		else:
			print("Thank you, goodbye.")
			sys.exit()
	except ValueError:
		print("You must enter an integer greater than 0.")
		sys.exit()