"""
Question
Write a program that uses a while loop to prompt the user for a series of numbers and check whether each number is divisble by 2, 3, 5 or 7.
Execution of the program continues until a negative number is entered.
Save this program as p8p1.py.

Pseudocode
while int is not negative:
     check if divisible by 2, 3, 5, 7 and let the user know
let user know the proces has stopped because a negative number is entered
"""

while True:
     try:
          num = 1
          while num > -1:
               num = int(input("Enter an integer: "))
               if num < 0:
                    break
               if num % 2 == 0:
                    print(str(num) + " is divisible by 2")
               else:
                    print(str(num) + " is not divisibley by 2")
               if num % 3 == 0:
                    print(str(num) + " is divisible by 3")
               else:
                    print(str(num) + " is not divisibley by 3")
               if num % 5 == 0:
                    print(str(num) + " is divisible by 5")
               else:
                    print(str(num) + " is not divisibley by 5")
               if num % 7 == 0:
                    print(str(num) + " is divisible by 7")
               else:
                    print(str(num) + " is not divisibley by 7")
               print("")#buffer
          break
     except ValueError:
          print("You did not enter an integer.  Please try entering an integer again.")

print("The process has stopped because a negative integer was entered.")