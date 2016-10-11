"""
QUESTION

Write a program that prompts the user for two numbers.
If the sum of the numbers is greater than 100, print "That is a big number!" and terminate the program.
"""


"""
PSEUDOCODE

Enter number 1
Enter number 2
Add number 1 and number 2
if 100 is less than the sum, print the message
otherwise, do nothing
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

#algorithm
if (100 < (num1 + num2)):
 print("That's a big number!")
else:
 pass