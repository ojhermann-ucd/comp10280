"""
QUESTION
Write a program that prompts the user for three numbers (ints), examines the numbers and prints out the largest odd number among them.
If none of them are odd, the program should print out a message to that effect.
The program should then terminate.
"""

"""
PSEUDOCODE

INPUTS
num1 = x
num2 = y
num3 = z
num_list = [num1, num2, num3]

ALGORITHM
sort num_list in descending value
starting at the start of the list:
 if number is odd, then print and end program
 else check next number;
if no number is odd, print a message saying so
"""

#user inputs
while True:
 try:
  num1 = int(input("Enter an integer value for number 1: "))
  num2 = int(input("Enter an integer value for number 2: "))
  num3 = int(input("Enter an integer value for number 3: "))
  break
 except ValueError:
  print("You did not enter appropriate values.  Please restart the program if you want to try again.")
  break
output_num = num1

#algorithm to submit
if (num1 % 2 != 0) and (num2 % 2 != 0):
 



#calculated inputs
num_list = [num1, num2, num3]
n_count = 0

#algorithm 1
num_list.sort(reverse = True)
for n in num_list:
 if n % 2 != 0:
  n_count += 1
  print(n)
  break
 else:
  pass

if n_count == 1:
 pass
else:
 print("No number entered is odd.")

 #algorithm 2
num_list.sort(reverse = True)
for n in num_list:
 if n % 2 != 0:
  print(n)
  break
 else:
  n_count += 1
  if n_count < len(num_list):
   pass
  else:
   print("No number entered is odd.")