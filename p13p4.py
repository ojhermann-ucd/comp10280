"""
Implement the program that illustrates scoping in Python from today’s lectures (Page 12 of the notes).
Save this program as p13p4.py.
"""

def f(x):
	"""
	Function that adds 1 to its argument and prints it out
	"""
	print("In function f: ")
	x += 1
	y = 1
	print("x is " + str(x))
	print("y is " + str(y))
	print("z is " + str(z))
	return x

x, y, z = 5, 10, 15

print("Before function f: ")
print("x is " + str(x))
print("y is " + str(y))
print("z is " + str(z))

z = f(x)

print("After function f: ")
print("x is " + str(x))
print("y is " + str(y))
print("z is " + str(z))