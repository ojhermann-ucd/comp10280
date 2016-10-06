while True:
 try:
  int_val = int(input("Enter an integer value: "))
  break
 except ValueError:
  print("You did not enter an integer; please try again.")

if int_val < 0:
 print(str(int_val) + " < 0.")
elif int_val == 0:
 print(str(int_val) + " == 0.")
elif int_val in range(0, 21, 1):
 print("0 <= " + str(int_val) + " <= 20.")
elif int_val in range(21, 41, 1):
 print("20 < " + str(int_val) + " <= 40.")
elif int_val in range(41, 61, 1):
 print("40 < " + str(int_val) + " <= 60.")
elif int_val in range(61, 81, 1):
 print("60 < " + str(int_val) + " <= 80.")
elif int_val in range(81, 101, 1):
 print("80 < " + str(int_val) + " <= 100.")
else:
 print(str(int_val) + " > 100")