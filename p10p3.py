"""
Write a program that prompts the user for a series of strings and counts and prints out the number of vowels (letters 'a', 'e', 'i', 'o' or 'u') in each string.
The program should exit when an empty string is entered.
Save this program as p10p3.py.

Pseudocode
user enters val
if val is empty:
     print message
     exit program
else:
     count vowels (upper and lower case)
     print the number of vowels counted
     start the program again
"""

while True:
     try:
          val = input("Please enter a string (enter nothing to exit the program): ")
          count_v = 0
          if not val:
               print("The program has exited because you entered nothing.")
               break
          else:
               for i in val:
                    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":#lists and other structures not allowed
                         count_v += 1
                    else:
                         pass
               print("There were " + str(count_v) + " vowels in your string.")
     except ValueError:
          print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
          break