"""
Write a program that uses a while loop to prompt the user for a series of integers and check whether each number is in one of the specified ranges:
• Number is equal to 0
• Number is greater than 0 and less than or equal to 20
• Number is greater than 20 and less than or equal to 40
• Number is greater than 40 and less than or equal to 60
• Number is greater than 60 and less than or equal to 80
• Number is greater than 80 and less than or equal to 100
• Number is greater than 100
The program should also count the number of numbers in each range.
The program should continue until the user enters a number that is less than 0.
Before finishing, the program should print out the analysis of the input, ie the number of numbers in each range.

Pseudocode
while (num  = user input number) positive integer:
     see which range it fall into and record that membership with a count
once negative number is entered:
     print counts for each range
     print announcement of what has happened
"""
#range counters
range_0_count = 0
range_1_20_count = 0
range_21_40_count = 0
range_41_60_count = 0
range_61_80_count = 0
range_81_100_count = 0
range_100_count = 0

while True:
     try:
          num = 1
          while num > -1:
               num = int(input("Enter an integer value, please (if you want to exit and see the summary, enter a negative integer): "))
               if num == 0:
                    range_0_count += 1
                    print(str(num) + " = 0")
               elif 0 < num <= 20:
                    range_1_20_count += 1
                    print("0 < " + str(num) + " <= 20")
               elif 20 < num <= 40:
                    range_21_40_count += 1
                    print("20 < " + str(num) + " <= 40")
               elif 40 < num <= 60:
                    range_41_60_count += 1
                    print("40 < " + str(num) + " <= 60")
               elif 60 < num <= 80:
                    range_61_80_count += 1
                    print("60 < " + str(num) + " <= 80")
               elif 80 < num <= 100:
                    range_81_100_count += 1
                    print("80 < " + str(num) + " <= 100")
               elif 100 < num:
                    range_100_count += 1
                    print("100 < " + str(num))
               else:
                    pass
          break
     except ValueError:
          print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
          break
#summary report
print("")#buffer
print("")#buffer
print("This is the summary of your entries")
print("x = 0: " + str(range_0_count) + " entries.")
print("0 < x <= 20: " + str(range_1_20_count) + " entries.")
print("20 < x <= 40: " + str(range_21_40_count) + " entries.")
print("40 < x <= 60: " + str(range_41_60_count) + " entries.")
print("60 < x <= 80: " + str(range_61_80_count) + " entries.")
print("80 < x <= 100: " + str(range_81_100_count) + " entries.")
print("100 < x: " + str(range_100_count) + " entries.")
print("")#buffer
print("")#buffer