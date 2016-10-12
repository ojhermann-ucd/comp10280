"""
QUESTION
Write a program that prompts the user for three numbers (ints), examines the numbers and prints out the largest odd number among them.
If none of them are odd, the program should print out a message to that effect.
The program should then terminate.
"""

"""
PSEUDOCODE
User inputs integers a, b, and c. (a more detailed explanation is after the code)

First Calculations
a + b + c
a + b
    b + c

Main Program
if a + b + c odd:
  if a + b odd:
    if b + c odd:
      return b
    else b + c even:
      return a
  else a + b even:
    if b + c odd:
      return c
    else a, b, and c are odd:
      if (b <= a) and (c <= a):
        return a
      elif (a <= b) and (c <= b):
        return b
      else:
        return c
if a + b + c even:
  if a + b odd:
    if b + c odd:
      if c <= a:
        return a
      else:
        return c
    else b + c even:
      if c <= b:
        return b
      else:
        return c
  else a + b even:
    if b + c odd:
      if b <= a:
        return a
      else:
        return b
    else b + c even:
      return "No odd numbers were input"
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

"""
DETAILED PSEUDOCODE
This solution is based on number properties when adding integers a, b, and c.

First Calculations
a + b + c
a + b
    b + c

Possible Odd/Even Outcomes for a + b + c
o + o + o = o
o + o + e = e
o + e + o = e
o + e + e = o
e + o + o = e
e + o + e = o
e + e + o = o
e + e + e = e

if a + b + c odd:
  o + e + e = o
  e + o + e = o
  e + e + o = o
  o + o + o = o
  if a + b odd:
    e + o + e = o
    o + e + e = o
    if b + c odd:
      return b
    else b + c even:
      return a
  else a + b even:
    e + e + o = o
    o + o + o = o
    if b + c odd:
      return c
    else a, b, and c are odd:
      if (b <= a) and (c <= a):
        return a
      elif (a <= b) and (c <= b):
        return b
      else:
        return c

if a + b + c even:
  o + e + o = e
  e + o + o = e
  o + o + e = e
  e + e + e = e
  if a + b odd:
    o + e + o = e
    e + o + o = e
    if b + c odd:
      if c <= a:
        return a
      else:
        return c
    else b + c even:
      if c <= b:
        return b
      else:
        return c
  else a + b even:
    o + o + e = e
    e + e + e = e
    if b + c odd:
      if b <= a:
        return a
      else:
        return b
    else b + c even:
      return "No odd numbers were input"
"""