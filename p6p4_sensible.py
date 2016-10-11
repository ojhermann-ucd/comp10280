"""
QUESTION
Write a password checking program to keep track of how many times a user has entered their password incorrectly.

Store a password in your program.
 If the user enters the password incorrectly more than three times, print "You have been denied access." and terminate the program
 If the password is correct, print "You have successfully logged in." and terminate the program.
"""

"""
PSEUDOCODE

user enters password:
 if the password is correct, print requested output
 if the password is incorrect and while count is less than 3
  increase count by 1 and allow them to try again
 else:
  print the deinal message
"""

#algorithm 1
password_real = "123"
count = 0
bound = 3

while count < bound:
 if input("Please enter the password: ") == password_real:
  print("You have successfully logged in.")
  break
 else:
  count += 1
  print("That is not the password.  Please try again.")

if count == 3:
 print("You have been denied access.")
else:
 pass