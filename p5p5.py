city_list = ["Dublin", "Belfast", "Cork", "Limerick", "Derry", "Galway", "Lisburn", "Kilkenny", "Waterford", "Sligo"]

while True:
 try:
  city_input = input("Enter the name of a town or city as a string: ")
  break
 except ValueError:
  print("You did not enter a town or city name as a string.")

if city_input in city_list:
 print("You entered " + city_input)
else:
 print("Sorry, I didn't recognise that name.")