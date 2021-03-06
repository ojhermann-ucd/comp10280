"""
QUESTION
Write a program that asks the user their name.

If they enter your name, print "That is a cool name!"

If they enter "Mickey Mouse" or "Spongebob Squarepants", tell them that you are not sure that that is their name.

Otherwise, tell them "You have a nice name."

The program should then terminate.
"""

"""
PSEUDOCODE

Inputs
my_name = s1
user_name = s2
bad_names = list(Mickey Mouse, Spongebob Squarepants)

Algorithm
Enter user name

if user_name == my_name:
 print "That is a cool name!"
elif user_name in bad_names:
 print "I do not think that is your name."
else:
 print "You have a nice name."
"""

#existing inputs
my_name = "Otto"
bad_names = ["Mickey Mouse", "Spongebob Squarepants"]

#user inputs
user_name = input("Enter your name: ")

#algorithm
if user_name == my_name:
 print("That is a cool name!")
elif user_name in bad_names:
 print("I do not think that is your name.")
else:
 print("You have a nice name.")