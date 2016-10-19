"""
Write a program that sums the integers in the range 1 - 10 000 that are divisble by 3 or by 5 and prints out the total.
Save this program as p7p5.py.

Pseudocode
define the range
for each element of the range:
     if element is divisible by 3 or 5:
          add it to the running sum
     else:
          nothing
print running sum

"""
#if the range in inclusive
range_min = 1
range_max = 10000
range_problem = range(range_min, range_max, 1)
sum_problem = 0
for i in range_problem:
     if (i % 3 == 0) or (i % 5 == 0):
          sum_problem += i
     else:
          pass
print(str(sum_problem) + " is the answer if the range does not include 10000 (as we would expect in Python).")
sum_problem += range_max
print(str(sum_problem) + " is the answer if the range does include 10000 (as we might expect in natural language).")



"""
#manual inputs
range_min = 0
range_max = 10000
multiples = [3, 5]
sum_list = []

#algorithm
for m in multiples:
     m_range = range(range_min, range_max, m)
     for r in m_range:
          if r not in sum_list:
               sum_list.append(r)
print(sum(sum_list))
print("This is a minor adjustment on Project Euler Problem 1, so I've put my solution to that problem in here.")
"""

