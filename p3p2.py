#manual inputs
length = 2.0000
pi = 3.1415927#estimate of pi

#calculated inputs
length = float(length)#making sure the variable is a floating point figure and compatible with Python2
pi = float(pi)#making sure the variable is a floating point figure and compatible with Python2
diameter = length
radius = float(diameter / 2)#making sure the variable is a floating point figure and compatible with Python2

#calculations
area_square = length ** 2

volume_cube = length ** 3

area_circle = pi * (radius ** 2)

volume_sphere = float(4 / 3) * pi * (radius**3)

volume_cylinder = area_circle * length

#outputs
print("The area of the square is " + str(area_square))
print("The volume of the cube is " + str(volume_cube))
print("The area of the circle is " + str(area_circle))
print("The volume of the sphere is " + str(volume_sphere))
print("The volume of the cylinder is " + str(volume_cylinder))