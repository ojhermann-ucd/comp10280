"""
Pseudocode
Take user inputs

if both same, return true

if not same, find which is shorter

if short string on end of longer string, return True; else return False

"""

#input strings
string1 = input("Please enter the first string: ").lower()
string2 = input("please enter the second string: ").lower()

def stringEnds(s1, s2):
	if s1 == s2:
		return True
	else:
		if len(s1) < len(s2):
			if s1 == s2[-len(s1) : len(s2) + 1 : 1]:
				return True
			else:
				return False
		else:
			if s2 == s1[-len(s2) : len(s1) + 1 : 1]:
				return True
			else:
				return False

print(stringEnds(string1, string2))