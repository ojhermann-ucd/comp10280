""""
Write a program that prompts the user for a series of integers and, for each of the numbers entered, performs exhaustive enumeration to find the integer cube root of the number.
If the number is not a perfect cube, the program should print out a message to that effect.
Note that the program should work for negative numbers as well as positive numbers.
The program should exit when a 0 is entered.
Save this program as p10p2.py.

Pseudocode
user enters num (make sure is integer)
if num = 0:
     exit program with message
else:
     if num > 0:
          starting with n = 0, check if num = n^3:
               if yes:
                    print result
                    start program again
               if no:
                    check n += 1 until n = num
               if the above results in nothing, print the number is not a perfect cube
               start program again
     if num < 0:
          starting with n = 0, check if num = n^3:
               if yes:
                    print result
                    start program again
               if no:
                    check n -= 1 until n = num
               if the above results in nothing, print the number is not a perfect cube
               start program again
"""

while True:
     try:
          num = int(input("Enter an integer, please (it should be small; we must use an exhaustive method): "))
          count = 0
          if num < 0:
               while num <= count**3:
                    if num != count**3:
                         count -= 1
                    else:
                         print(str(num) + " = " + str(count) + "^3")
                         break
               else:
                    print(str(num) + " is not a perfect cube.")
          elif num > 0:
               while count**3 <= num:
                    if num != count**3:
                         count += 1
                    else:
                         print(str(num) + " = " + str(count) + "^3")
                         break
               else:
                    print(str(num) + " is not a perfect cube.")
          else:
               print("You entered zero so the program has exited.")
               break
     except ValueError:
          print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
          break