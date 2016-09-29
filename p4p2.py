import math

#manual inputs
length = float(input("Enter the length of the side: "))

#calculations
area_square = length ** 2

volume_cube = length ** 3

area_circle = math.pi * (length ** 2)

volume_sphere = float(4 / 3) * (float(math.pi) * (length ** 3))

volume_cylinder = area_circle * length

#outputs
print("The area of the square with side length " + str(length) + " is " + str(area_square))
print("The volume of the cube is with side length "  + str(length) + " is " + str(volume_cube))
print("The area of the circle with radius " + str(length) + " is " + str(area_circle))
print("The volume of the sphere with radius " + str(length) + " is " + str(volume_sphere))
print("The volume of the cylinder with radius " + str(length) + " and length " + str(length) + " is " + str(volume_cylinder))