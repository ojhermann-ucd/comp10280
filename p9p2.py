"""
Write a program that prompts the user for a series of integers and, for each of the numbers entered, uses a for loop to calculate the sum of the integers up to and including that number.
The program should stop when a non-positive number is entered.

Pseudocode
user enters num
if num > -1:
     for n in range zero to num inclusive:
          starting from n = zero, add n to total
          increment n
          repeat until we have added n = num
     make have prompt repeat
if num < 0:
     exit the program

"""

while True:
     try:
          num = int(input("Enter an integer value, please (if you want to exit, enter a negative integer): "))
          if num < 0:
               print("You entered a negative integer and have exited the program")
               break
          else:
               while num > -1:
                    start = 0
                    num_range = range(start, num + 1, 1)
                    num_sum = 0
                    for n in num_range:#REQUESTED FOR LOOP
                         num_sum += n
                    print("The sum of " + str(start) + " to " + str(num) + " is " + str(num_sum))
                    break
     except ValueError:
          print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
          break