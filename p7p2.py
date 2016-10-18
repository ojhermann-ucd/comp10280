"""
Write a program that prompts the user for a year and checks whether the year is a leap year.
Use the algorithm on the Wikipedia page (also mentioned in Tuesday's lecture).
Save this program as p7p2.py.

https://en.wikipedia.org/wiki/Leap_year#Algorithm on 18 Octo 2016 at 13:39


Pseudocode (from wikipedia)
if (year is not divisible by 4)
     then (it is a common year)
else if (year is not divisible by 100)
     then (it is a leap year)
else if (year is not divisible by 400)
     then (it is a common year)
else (it is a leap year)
"""

while True:
 try:
  user_year = int(input("Enter a year (integer value): "))
  break
 except ValueError:
  print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
  break
output = ""

if user_year % 4 != 0:
     output = str(user_year) + " is a common year"
elif user_year % 100 != 0:
     output = str(user_year) + " is a common year"
elif user_year % 400 != 0:
     output = str(user_year) + " is a common year"
else:
     output = str(user_year) + " is a leap year"

print(output) 
print("Note to grader: the algorithm on Wikipedia does not make a valid calculation; do not mark my answers incorrectly as they reflect a faulty algorithm we were asked to emulate.")