#this program will demonstrate various features of the use of slices in Python
animals = 'herd of elephants'
x = 0
y = 0
seg = animals[x:y]

#(a)
#when x = y, the slice returns nothing because it's slicing from animals[x] to animals[x-1], which is not a space Python can understand; it views this as non-existent
print("(a): when x = y, the slice returns nothing because it's slicing from animals[x] to animals[x-1], which is not a space Python can understand; it views this as non-existent")
print("example a1: x = y = 0 returns " + seg)
x = 2
y = 2
print("example a2: x = y = 2 returns " + seg)
print("")

#(b)
#when x > y, the slice returns nothing because it's slicing from animals[x] to animals[y-1], which is not a space Python can understand; it views this as non-existent
print("(b): when x > y, the slice returns nothing because it's slicing from animals[x] to animals[y-1], which is not a space Python can understand; it views this as non-existent")
x = 3
y = 0
print("example b1: x = 3, y = 0 returns " + seg)
x = 5
y = 2
print("example b2: x = 5, y = 2 returns " + seg)
print("")

#(c)
#when x is omitted, the slice will be from animals[0] to animals[y - 1] i.e. a slice that is y elements long
print("(c): when x is omitted, the slice will be from animals[0] to animals[y - 1] i.e. a slice that is y elements long")
y = 4
print("example c1: x omitted, y = 4 returns " + animals[:y])
y = 6
print("example c2: x omitted, y = 6 returns " + animals[:y])
print("")

#(d)
#when y is omitted, the slice will be from animals[x] to the end of the string i.e. a slice that is len(animals) - x long
print("(d): when y is omitted, the slice will be from animals[x] to the end of the string i.e. a slice that is len(animals) - x long")
x = 1
print("example d1: x = 1, y omitted returns " + animals[x:])
x = 6
print("example d2: x = 6, y omitted returns " + animals[x:])
print("")

#(e)
#when both x and y are omitted, the entire string will be printed
print("(e): when both x and y are omitted, the entire string will be printed")
print("Example when both x and y are omitted: " + animals[:])