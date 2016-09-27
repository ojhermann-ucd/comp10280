#manual inputs
currency1 = 4.0000#currency 1 value
currency1_type = "GBP"#currency 1
currency2_type = "USD"#currency 2
rate = 1.3000#exchange rate

#calculated inputs
currency1 = float(currency1)#making sure the variable is a floating point figure and compatible with Python2
rate = float(rate)#making sure the variable is a floating point figure and compatible with Python2

#calculation
currency2 = float(currency1 * rate)#currency 2 value

#print result
print(currency1_type + " " + str(currency1) + " = " + currency2_type + " " + str(currency2))