"""
QUESTION
Write a program that prompts the user for three numbers (ints), examines the numbers and prints out the largest odd number among them.
If none of them are odd, the program should print out a message to that effect.
The program should then terminate.
"""

"""
PSEUDOCODE
This is based on number properties when adding integers.

Three numbers: a, b, c
if a + b + c is odd (then one or three of the numbers is odd):
 if a + b is odd:
  if b + c is odd: return b
  else (b + c is even): return a
 else (a + b is even):
  if b + c is odd: return c
  else (must compare magnitudes because all numbers are odd):
   if a > b:
    if a > c: return a
    else:
     if c > a: return c
     else: return a or c (a = c)
   else:
    if b > a:
     if b > c: return b
     else:
      if c > b: return c
      else: return b or c (b = c)
   else: return a or b or c (a = b = c)

else (a + b + c is odd, meaning one or three numbers is even):
 if a + b even:
  if b + c odd: return 
  .
  .
  .

See comments below for clarification
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

#calculated inputs
num123 = num1 + num2 + num3
num12 = num1 + num2
num13 = num1 + num3
num23 = num2 + num3

if (num123 % 2 != 0):#sum of three numbers is odd
  if (num12 % 2 != 0) and (num23 % 2 != 0):#sum of first two and sum of last two both odd
    print(num2)
  elif (num12 % 2 != 0) and (num23 % 2 == 0):#sum of first two odd and sum of last two even
    print(num1)
  elif (num12 % 2 == 0) and (num23 % 2 != 0):#sum of first two even and sum of last two odd
    print(num3)
  else:#sum of first two even and sum of last two even
    if (num1 <= num2 <= num3) or (num2 <= num1 <= num3):#making sure num3 is the biggest
      print(num3)
    elif (num1 <= num3 <= num2) or (num3 <= num1 <= num2):#making sure num3 is the biggest
      print(num2)
    else:
      print(num1)
else:#sum of three numbers is even
  if (num12 % 2 == 0) and (num23 % 2 == 0):#sum of first two is even and sum of last two is even
    print("No odd numbers were given.")
  elif (num12 % 2 == 0) and (num23 % 2 != 0):#sum of first two is even and sum of last two is odd
    if num1 <= num2:
      print(num2)
    else:
      print(num1)
  elif (num12 % 2 != 0) and (num23 % 2 == 0):#sum of first two is odd and sum of last two is even
    if num2 < num3:
      print(num3)
    else:
      print(num2)
  else:#sum of first two is odd and sume of last two is odd
    if num1 < num3:
      print(num3)
    else:
      print(num1)