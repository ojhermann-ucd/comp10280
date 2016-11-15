"""
Pseudocode
define function that finds divisors for a given interger input:
- negative function
- positive function

define fucntion that determines if number is perfect (one for both pos and neg inputs):
- if sume of output of first function is equal to input, return True; else False

define a fucntion that, for a given input (positive and negative), prints each number up to the input:
- pos: for i in range 0 to input, if perfect, append to list
- neg: for i in range input to -1, if perfect, append to list
- in both cases, return the list

"""


import sys

def posDivs(n):
	divRange = range(1, n, 1)
	output = [i for i in divRange if n % i == 0]
	return output

def posNum(n):
	if sum(posDivs(n)) == n:
		return True
	else:
		return False

def posNums(n):
	pRange = range(0, n + 1, 1)
	output = []
	for i in pRange:
		if posNum(i):
			output.append(i)
		else:
			pass
	return output


def negDivs(n):
	divRange = range(-1, n, -1)
	output = [i for i in divRange if n % i == 0]
	return output

def negNum(n):
	if sum(negDivs(n)) == n:
		return True
	else:
		return False

def negNums(n):
	pRange = range(0, n -1, -1)
	output = []
	for i in pRange:
		if negNum(i):
			output.append(i)
		else:
			pass
	return output

while True:
	try:
		num = int(input("Please enter an integer (or something else to exit): "))
		if 0 < num:
			print("The perfect numbers up to", str(num), "are", posNums(num))
		else:
			print("The perfect numbers up to", str(num), "are", negNums(num))
	except ValueError:
		print("You must enter an integer.")
		sys.exit()