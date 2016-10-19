"""
Write a program that prompts the user for a year and checks whether the year is a leap year.
Use my algorithm from Tuesday's lecture.
Save this program as p7p1.py.

Note: Algorithm taken from Lecture 8 Slide; attributed to Wikipedia, but told by TA to use this one for p7p1.py

Pseudocode
if year ≥ 0:
     if (year mod 4 = 0 and year mod 100 != 0) or (year mod 400 = 0):
          leap year
     else:
          common year
else:
     year must be ≥ 0
"""

while True:
 try:
  user_year = int(input("Enter a year (integer value): "))
  break
 except ValueError:
  print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
  break
output = ""

if user_year > 0:
     if ((user_year % 4 == 0) and (user_year % 100 != 0)) or (user_year % 400 == 0):
          output = str(user_year) + " is a leap year"
     else:
          output = str(user_year) + " is a common year"
else:
     output = str(user_year) + " is negative . . . you must enter a positive value for year"

print(output)
print("Note: Algorithm taken from Lecture 8 Slide; attributed to Wikipedia, but told by TA to use this one for p7p1.py")