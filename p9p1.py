"""
Write a program that prompts the user for an integer and uses a while loop to calculate the sum of the integers up to and including that number.

Pseudocode
Make sure the user put in a valid num
if num is positive:
     starting from n = zero, add n to total
     increment n
     repeat until we have added n = num
if num is negative:
     starting from n = num, add n to total
     increment n
     repeat until we have adde n = 0
"""

while True:#making sure an appropriate value is entered
 try:
  num = int(input("Enter an integer value: "))
  break
 except ValueError:
  print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
  break


if num > -1:
     start = 0
     num_sum = 0
     adder = 0
     while adder < num + 1:#REQUESTED WHILE LOOOP
          num_sum += adder
          adder += 1
     print("The sum of " + str(start) + " to " + str(num) + " is " + str(num_sum))
else:
     end = 0
     num_sum = 0
     adder = 0
     while adder > num - 1:#REQUESTED WHILE LOOOP
          num_sum += adder
          adder -= 1
     print("The sum of " + str(num) + " to " + str(end) + " is " + str(num_sum))





"""
     num_range = range(start, num + 1, 1)
     for n in num_range:
          num_sum += n
     print("The sum of " + str(start) + " to " + str(num) + " is " + str(num_sum))

else:
     end = 0
     num_range = range(end, num - 1, -1)
     num_sum = 0
     for n in num_range:
          num_sum += n
     print("The sum of " + str(num) + " to " + str(end) + " is " + str(num_sum))
"""