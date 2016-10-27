"""
Write a program that prompts the user for an integer and performs exhaustive enumeration to find the integer square root of the number.
By "exhaustive enumeration", we mean that we start at 0 and succcessively go through the integers, checking whether the square of the integer is equal to the number entered.
If the number is not a perfect square, the program should print out a message to that effect.
The program should exit when a negative number is entered.
Save this program as p10p1.py.

Pseudocode
user enters num (make sure is integer)
if num < 0:
     exit program with message
else:
     starting with n = 0, check if num = n^2:
          if yes:
               print result
               start program again
          if no:
               check n += 1 until n = num
          if the above results in numthing, print the number is not a perfect square
          start program again
"""

while True:
     try:
          num = int(input("Enter an integer, please (it should be small; we must use an exhaustive method): "))
          if num > -1:
               count = 0
               while count**2 <= num:
                    if num != count**2:
                         count += 1
                    else:
                         print(str(num) + " = " + str(count) + "^2")
                         break
               else:
                    print(str(num) + " is not a perfect square.")
          else:
               print("You entered a negative integer so the program has exited.")
               break
     except ValueError:
          print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
          break