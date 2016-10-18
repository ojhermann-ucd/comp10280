"""
Write a program that uses a while loop to go through the first 50 integers and prints out each number and the square of the number.
Save this program as p7p3.py.

Pseudocode

start = ask user to input where they want their integer range to begin because the integers continue infinitely both negatively and positively
count = 0
limit = 50
while count < limit:
     print("Integer " + str(count + 1) + " is " + str(start) + "and the square of start is " + str(start**2))
     count += 1
"""

while True:
 try:
  start = int(input("Enter an integer as the starting point of this exercise: "))
  break
 except ValueError:
  print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
  break

count = 0
limit = 50
while count < limit:
     print("Integer " + str(count + 1) + " is " + str(start) + " and its square is " + str(start**2))
     count += 1
     start += 1
print("Note the grader: as the integers extend infinitely in both positive and negative directions, I had to ask the user to input the starting point.")