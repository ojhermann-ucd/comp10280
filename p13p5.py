"""
Add some extra variables and operations on those variables in the program from the previous question to ensure
that you understand what is going on and how it works.
Save this program as p13p5.py.
"""

def f(x):
	"""
	Function that adds 1 to its argument and prints it out
	"""
	print("In function f: ")
	x += 1
	y = 1
	j = 2
	print("x is " + str(x))
	print("y is " + str(y))
	print("z is " + str(z))
	print("h is " + str(h) + " in the function because it wasn't manipulated by the function, so it's global value was assigned")
	print("j is " + str(j) + " in the function because within the funciton that value was assigned")
	return x

x, y, z, h, j = 5, 10, 15, 99, 80000

print("Before function f: ")
print("x is " + str(x))
print("y is " + str(y))
print("z is " + str(z))
print("h is " + str(h) + " at the start")
print("j is " + str(j) + " at the start")

z = f(x)

print("After function f: ")
print("x is " + str(x))
print("y is " + str(y))
print("z is " + str(z))
print("h is " + str(h) + " at the end")
print("j is " + str(j) + " yet again because the prior change was only within the scope of the function, not global")