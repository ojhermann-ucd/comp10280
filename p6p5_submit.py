"""
Question

Ask the user to enter a password.
 If the password is correct (ie it matches the password stored in the program), print "You have successfully logged in." and terminate the program.
 If the password is wrong print "Sorry, the password is wrong." and ask the user to enter the password three times.
  If the user enters the correct password three times, print "You have successfully logged in." and terminate the program; otherwise print "You have been denied access." and terminate the program.
"""


"""
Pseudocode

user enters a password
if is matches the actual password, print the output
if it does not match the actual password, instruct them to enter the correct password three times
if this is done successfully, prin the desired output; otherwise the nasty message
"""

password_real = "1234"
count = 0
bound = 3

if input("Please enter the password: ") == password_real:
 print("You have successfully logged in.")
else:
 print("That was not the password.  You must now enter the correct password three times.")
 while count < bound:
  if input("Please enter the password.  This is entry " + str(count+1) + "/" + str(bound) + ": ") == password_real:
   count += 1
  else:
   print("You have been denied access.")
   break

if count == 3:
 print("You have successfully logged in.")
else:
 pass