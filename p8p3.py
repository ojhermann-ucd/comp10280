"""
Write a program that uses a while loop to generate a simple multiplication table from 0 to 20.

Pseudocode
num = user input integer
count = 0
print(str(num) + " Times Table for 0 to 20")
while count < 21:
     print(count, end = " x ")
     print(num, end = " = ")
     print(count * num)

"""

while True:
 try:
  num = int(input("Enter an integer value, please: "))
  count = 0
  print("Times Table for " + str(num) + " from 0 to 20")
  while count < 21:
     count_len = len(str(count))
     if count_len < 2:
          print(count, end = "  x ")#double space before the x to align the x symbols
          print(num, end = " = ")
          print(count * num)
          count += 1
     else:
          print(count, end = " x ")
          print(num, end = " = ")
          print(count * num)
          count += 1
  break
 except ValueError:
  print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
  break