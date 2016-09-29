#manual inputs
amount = float(input("Enter the initial amount here: "))
amount_larger_pct = float(6) / float(10)
tax_larger_pct = float(135) / float(1000)
tax_smaller_pct = float(23) / float(100)

#calculated inputs
amount_larger = amount * amount_larger_pct
amount_smaller = (amount - amount_larger)
amount_larger_tax = amount_larger * tax_larger_pct
amount_smaller_tax = amount_smaller * tax_smaller_pct

#calculation
total = amount_larger + amount_larger_tax + amount_smaller + amount_smaller_tax

#output
print("Initial Amount: " + str(amount))
print("60% of " + str(amount) + " is " + str(amount_larger) + ", resulting in tax of " + str(amount_larger_tax) + " at a rate of " + str(tax_larger_pct))
print("40% of " + str(amount) + " is " + str(amount_smaller) + ", resulting in tax of " + str(amount_smaller_tax) + " at a rate of " + str(tax_smaller_pct))
print("The total tax is " + str(amount_larger_tax + amount_smaller_tax))
print("The total amount is " + str(amount + amount_larger_tax + amount_smaller_tax))