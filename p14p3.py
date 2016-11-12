"""
Pseudocode for this algorithm was given in the lecture slide referenced in the problem

This is a nice way to check if a number is prime without storing a list of prime numbers.

This mememory efficient approach of using a range vs. a list, is efficient.

A range generates a number when it is to be iterated over, while a list would create all the numbers to be iterated, save them in a list, and then iterate over them.

This method is less memory intense.
"""
for num in range(2, 20, 1):
	for i in range(2, num, 1):
		if num % i == 0:
			print(str(num) + " = " + str(i) + " * " + str(num // i))
			break
	else:
		print(str(num) + " is a prime number")
print("Finished!")
print("note: this was taken and not modified from the lecture notes")
print("note: there are failings of this method e.g. it would treat 1 as a prime number")
print("note: I have not corrected problems as that was not in the problem request")