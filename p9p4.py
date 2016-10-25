"""
Write a program that prompts the user for a series of integers and, for each of the numbers entered, uses a while loop to calculate the factorial of that number.
The program should stop when a negative number is entered.

Pseudocode
user enters num (make sure is integer)
if num < 0:
     let user know to enter a positive number next time
else:
     if n = 0:
          return 1
     else:
          return n*factorial(n-1)
"""

while True:
     try:
          num = int(input("Enter a positive integer value, please (enter a negative number to exit the program): "))
          if num < 0:
               print("You entered a negative integer and have exited the program")
               break
          else:
               while num > -1:
                    fac = 1
                    if num == 0 or num == 1:
                         print(str(num) + "! = " + str(fac))
                    else:
                         mult = 1
                         while mult < num + 1:#REQUESTED WHILE LOOP
                              fac *= mult
                              mult += 1
                         print(str(num) + "! = " + str(fac))
                    break
     except ValueError:
          print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
          break