"""
Write a program that sums the integers in the range 1 - 10 000 that are divisble by 3 or by 5 and prints out the total.
Save this program as p7p5.py.

Pseudocode
define the range
for each element of the range:
     if element is divisible by 3 or five:
          add it to the running sum
     else:
          nothing
print running sum

"""
range_min = 1
range_max = 10000
range_problem = range(1, 10000, 1)
sum_problem = 0
for i in range_problem:
     if (i % 3 == 0) or (i % 5 == 0):
          sum_problem += i
     else:
          pass
print(sum_problem)

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

