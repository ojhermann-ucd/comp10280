"""
Pseudocode
make a recursively defined fib fnc
make another fnc that returns the value of the recursive fib fnc for each value up to and including the selected number

Note: just below would be my preferred recursive function for the fib sequence in python

import functools
@functools.lru_cache(None)
def fib(n):
	if n < 2:
		return n
	else:
		return fib(n - 1) + fib(n - 2)
"""


import sys

#recursive calculation of a Fib num
def recFib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return recFib(n - 2) + recFib (n - 1)

#function to display a fib sequence
def recFibSeq(p):
	for i in range(0, p + 1, 1):
		print("fib(" + str(i) + ") = " + str(recFib(i)))
	return "I would have used @functools.lru_cache(None) to make this quick, but I assuem that is off limits in this course"

while True:
	try:
		num = int(input("enter a non-negative integer (or negative integer to quit): "))
		if -1 < num:
			print(recFibSeq(num))
		else:
			print("Thank you, good bye.")
			print("")
			sys.exit()
	except ValueError:
		print("That was not an integer.")
		print("")
		sys.exit()