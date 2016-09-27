#manual inputs
amount = float(100)#making sure the variable is a floating point figure and compatible with Python2
amount_A_pct = float(6) / float(10)#making sure the variable is a floating point figure and compatible with Python2
tax_A_pct = float(135) / float(1000)#making sure the variable is a floating point figure and compatible with Python2
tax_B_pct = float(23) / float(100)#making sure the variable is a floating point figure and compatible with Python2

#calculated inputs
amount_A = amount * amount_A_pct
amount_B = (amount - amount_A)
amount_A_tax = amount_A * tax_A_pct
amount_B_tax = amount_B * tax_B_pct

#calculation
total = amount_A + amount_A_tax + amount_B + amount_B_tax

#output
print("A pre-tax cost of " + str(amount) + " results in an after tax total of " + str(total))