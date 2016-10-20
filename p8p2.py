"""
Write a program that prompts the user for a number and uses a while loop to generate the "multiplication table" for that number from 1 up to the number.

Pseudocode
Note: I added formatting to the algorithm under the constraint of using techniques we've been introduced to in class
Note: This might make the code less easy to read, but I've added comments to help clarify what's going on
Note: pseudocode was written without formatting included and is much simpler to follow

limit = user input integer
row_val = 0
col_val = 0
while row_val < limit + 1:
  while col_val < limit + 1:
    print(row_val * col_val, end = " ")
    col_val += 1
  col_val = 0
  print("")
  row_val += 1
"""

while True:
 try:
  limit = int(input("Enter an integer value, please (digits less than 12 tend to fit on a standard screen): "))
  #determining formatting parameters
  unit_width = len(str(limit * limit)) + 4
  space_count = 0
  column_one_width = len(str(limit))

  #print the multiplication sign in the top corner of the table
  print("x", end = "")
  while space_count < (column_one_width + 1) - len("x"):
       print(" ", end = "")
       space_count += 1
  space_count = 0
  #print the multipliers in the top row
  row_val = 0
  while row_val < limit + 1:
       while space_count < (unit_width + 1) - len(str(row_val)):
            print(" ", end = "")
            space_count += 1
       space_count = 0
       print(row_val, end = "")
       row_val += 1
  print("")
  #populate the rest of the table
  row_val = 0
  while row_val < limit + 1:
       print(row_val, end = "")#this is the other half of the multiplier
       while space_count < (column_one_width + 1) - len(str(row_val)):
            print(" ", end = "")
            space_count += 1
       space_count = 0
       col_val = row_val
       row_val += 1
       for r in range(0, limit + 1, 1):
            while space_count < (unit_width + 1) - len(str(col_val * r)):
                 print(" ", end = "")
                 space_count += 1
            space_count = 0
            print(col_val * r, end = "")
       print("")
  break
 except ValueError:
  print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
  break

