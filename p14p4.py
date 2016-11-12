"""
Pseudocode
make sure start, end are non-negative integers

calculate the range

if number in range is 0 or 1:
	print number = number x number
else:
	prime = 1
	for div in range(2, num, 1):
		if num divisible by div:
			print appropriate message
			multiply prime by 0
		else:
			pass
	if prime == 1:
		print appropriate message

Note: I've included two programs: one with redundant factor pairs, one without
"""

import sys

#user input variables
while True:
	try:
		#start of the range
		start = int(input("Enter the start of the range (non-negative integer): "))
		if start < 0:
			print("You must enter a non-negative integer.")
			sys.exit()
		#end of the range
		end = int(input("Enter the end of the range (non-negative integer larger than the start . . . Python conventions): "))
		if end < 0:
			print("You must enter a non-negative integer.")
			sys.exit()
		break
	except ValueError:
		print("You must enter a non-negative integer.")
		sys.exit()

#calculated variables
num_range = range(start, end, 1)

#program: redundant pairs
for num in num_range:
	if num in range(0, 2, 1):
		print(str(num) + " = " + str(num) + " * " + str(num))
	else:
		prime = 1
		for div in range(2, num, 1):
			if num % div == 0:
				print(str(num) + " = " + str(div) + " * " + str(num // div))
				prime *= 0
			else:
				pass
		if prime == 1:
			print(str(num) + " is a prime number")
print("NOTE: the program just run includes redundant factor pairs")
print("")

#program2: non-redundant pairs
for num in num_range:
	if num in range(0, 2, 1):
		print(str(num) + " = " + str(num) + " * " + str(num))
	else:
		prime = 1
		for div in range(2, num, 1):
			if div > (num // div):
				break
			else:
				if num % div == 0:
					print(str(num) + " = " + str(div) + " * " + str(num // div))
					prime *= 0
				else:
					pass
		if prime == 1:
			print(str(num) + " is a prime number")
print("NOTE: this program removed redundant factor pairs; look above to see the output for a program that included redundant factors pairs.")