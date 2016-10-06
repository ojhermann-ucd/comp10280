#manual inputs
currency1_val = float(input("Input the amount of currency 1: "))

#calculation
if currency1_val < 0:
 print("Amount must be >= 0. Please try again.")
else:
 exchange_rate = float(input("Input the exchange rate: "))
 currency2_val = float(currency1_val * exchange_rate)
 print(str(currency1_val) + " of currency 1 is worth " + str(currency2_val) + " of currency 2.")