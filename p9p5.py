"""
On any given day, a pizza company offers the choice of a certain number of toppings for its
pizzas. Depending on the day, it provides a fixed number of toppings with its standard pizzas.
Write a program that prompts the user (the manager) for the number of possible toppings
and the number of toppings offered on the standard pizza and calculates the total number of
different combinations of toppings. Recall that the number of combinations of k items from
n possibilities is given by the formula nCk = n! / k!(n - k)! .

Pseudocode
have user enter appropriate values for availTops and stanTops
calculate the factorial for:
     stanTops, availTops, and their difference
          if n = 0:
               return 1
          else:
               return n*factorial(n-1)
     input these values into the nCk formula and print the result

"""

while True:
     try:
          availTops = int(input("Enter the number of available toppings, please: "))
          stanTops = int(input("Enter the standard number of toppings, please: "))
          break
     except ValueError:
          print("You did not enter an appropriate value.  Please restart the program if you want to try again.")
          break

if (availTops > -1 and stanTops > -1) and (availTops > stanTops):
     #availTops!
     startAT = 1
     num_rangeAT = range(startAT, availTops + 1, 1)
     availTopsFac = 1
     for n in num_rangeAT:
          availTopsFac *= n
     #stanTops!
     startST = 1
     num_rangeST = range(startST, stanTops + 1, 1)
     stanTopsFac = 1
     for n in num_rangeST:
          stanTopsFac *= n
     #difference! . . . functions are very nice . . . as are recursively definced procedu)res
     dif = availTops - stanTops
     difST = 1
     num_rangeDif = range(difST, dif + 1, 1)
     difFac = 1
     for n in num_rangeDif:
          difFac *= n
     #number of combinations
     combos = int(availTopsFac / (stanTopsFac * difFac))
     print("The number of combinations of standard toppings (" + str(stanTops) + ") given the available toppings (" + str(availTops) + ")is " + str(combos))
elif (availTops == 0 or stanTops == 0) and (availTops > -1 and stanTops > -1):
     print("If either the number of available topping is zero or the standard number of toppings is zero, you can have only one type of pizza . . . bread.")
else:
     print("Your values for the available toppings and standard number of toppings is suspect.  Please try again.")