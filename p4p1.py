#manual inputs
currency_1_name = input("Enter the identifying symbol of the original currency: ")
currency_1_val = float(input("Enter the amount of the original currency: "))
currency_2_name = input("Enter the identifying symbol of the other currency: ")
exchange_rate = float(input("Enter the exchange rate between " + currency_1_name + " and " + currency_2_name + ": "))

#calculations
currency_2_val = round(float(currency_1_val * exchange_rate), 2)

#output
print("With an exchange rate of " + str(exchange_rate) + ", " + currency_1_name + str(currency_1_val) + " = " + currency_2_name + str(currency_2_val))