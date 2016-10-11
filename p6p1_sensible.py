"""
QUESTION
Write a program that prompts the user for two numbers.
If the sum of the numbers is greater than 100, print "That is a big number!" and terminate the program.
"""


"""
PSEUDOCODE

num1 = x
num2 = y
num_sum = num1 + num2
bound = 100

if (bound < num12):
 print("That is a big number!")
else:
 do nothing
"""

#user inputs
while True:
 try:
  num1 = float(input("Enter a value for number 1: "))
  num2 = float(input("Enter a value for number 2: "))
  break
 except ValueError:
  print("You did not enter appropriate values.  Please restart the program if you want to try again.")
  break

#calculated inputs
num_sum = num1 + num2

#algorithm
if (100 < num_sum):
 print("That's a big number!")
else:
 pass