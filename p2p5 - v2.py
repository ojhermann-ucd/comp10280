animals = 'herd of elephants'# randomly chosen string
len_animals = len(animals)#length of the randomly chosen string
range_animals = range(0, len_animals +1)

for x in range_animals:
 for y in range_animals:
  if not list(animals[x:y:1]):
   print("animals[x:y:1] for x = " + str(x) + " and y = " + str(y) + " is empty")
  else:
   print("animals[x:y:1] for x = " + str(x) + " and y = " + str(y) + " is " + animals[x:y:1])