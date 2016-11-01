"""
Taking the program to calculate the factorial of a number presented in class, 
investigate how it would be possible to have just two cases, one where the number is less than 0 and one where it isn’t. 
Rewrite the program to do this.
Save this program as p11p1.py.

Pseudocode

"""

while True:
     try:
          num = int(input("Enter a positive integer value, please: "))
          break
     except ValueError:
          print("Restart the program and enter a positive integer if you wish to continue.")
          break

if num < 0:
     print("Restart the program and enter a positive integer if you wish to continue.")
else:
	fac = 1
	count = num
	while 1 < count:
		fac *= count
		count -= 1
	print(str(num) + "! = " + str(fac))

print("Note: Professor Dunnion confirmed that this problem request us to modify p9p3.py to a two condition, not three condition factorial program")