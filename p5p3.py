while True:
 try:
  float_val = float(input("Enter a floating point value: "))
  break
 except ValueError:
  print("You did not enter a floating point value; please try again.")

if float_val < 0.00:
 print(str(float_val) + " is less than zero.")
elif float_val > 0.00:
 print(str(float_val) + " is greater than zero.")
else:
 print(str(float_val) + " is equal to zero.")