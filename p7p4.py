"""
Write a program that uses a while loop to sum the first 5000 integers and prints out the total.
Save this program as p7p4.py.

Pseudocode
count = 0
end = 5000
sum = 0
while the count is less than or equal to the end:
     sum += count
     count += 1
"""

end = 5000
count = 0
se_sum = 0

while count < end + 1:
     se_sum += count
     count += 1

print(se_sum)

"""
testfig = 0
for i in range(0, 5001, 1):
     testfig += i
print(testfig)

print(5001 * 2500)
"""
