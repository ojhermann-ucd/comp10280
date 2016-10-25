"""
Write a program that prompts the user for an integer and uses a for loop to calculate the factorial of that number.

Pseudocode
user enters num (make sure it's valid)
if num < 0:
     let user know to enter a positive value
else:
     if n = 0:
          return 1
     else:
          return n*factorial(n-1)
"""

while True:
     try:
          num = int(input("Enter a positive integer value, please: "))
          break
     except ValueError:
          print("Restart the program and enter a positive integer if you wish to continue.")
          break

if num < 0:
     print("Restart the program and enter a positive integer if you wish to continue.")
else:
     fac = 1
     if num == 0 or num == 1:
          print(str(num) + "! = " + str(fac))
     else:
          for n in range(1, num + 1, 1):#REQUESTED FOR LOOOP
               fac *= n
          print(str(num) + "! = " + str(fac))