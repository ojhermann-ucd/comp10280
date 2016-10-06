while True:
 try:
  int_val = int(input("Enter an integer value: "))
  break
 except ValueError:
  print("You did not enter an integer; please try again.")

if int_val < 0:
 print(str(int_val) + " is negative.")
else:
 print(str(int_val) + " is positive.")