"""
Pseudocode
create list of items we want to find, count, and compare
create associated index list

on each line:
- count each bracket and associated partner
- keep a running tally

compare the counts and report accordingly
"""
import sys
import os
import datetime

#list of strings to find in the document
sList = ["(", ")", "[", "]", "{", "}", "<", ">"]
countList = [] #i would have liked ot use a dictionary
for i in sList:
	countList.append(0)

#files
readFile = "p19p3read.txt"
recordFile = "p19p3record.txt"

#existence variables
readExist = os.path.isfile(readFile)
recordExist = os.path.isfile(recordFile)

#existence checks
if not readExist:
	print(readFile, "does not exists.")
	sys.exit()
if not recordExist:
	recordFile = open(recordFile, "w")
	recordFile.close()

#program
with open(readFile, "r") as reader:
	with open(recordFile, "a+") as writer:
		
		writer.write("in file ")
		writer.write(readFile) #identify the file
		writer.write("\n") #add a line after
		writer.write("at ")
		writer.write(str(datetime.datetime.now())) #add the datetime
		writer.write("\n") #add a line
		
		#count the shit
		for line in reader:
			for i in sList:
				countList[sList.index(i)] += line.count(i)

#not necessary, but keeping for kicks
with open(recordFile, "a+") as writer:
	for i in range(0, len(sList), 1):
		writer.write(str(sList[i])) #show character of interest; using str() in case future list contains non-string characters
		writer.write(" occurs ")
		writer.write(str(countList[i])) #show count of character of interest
		writer.write(" times.")
		writer.write("\n")
	writer.write("\n")

#total count section
print("")
print("This section reports on the total occurances of the relevant brackets")
for i in range(0, len(sList), 2): #compare each even indexed object with the next time, which by construction is its pair
	print(sList[i], "occurs", countList[i], "and", sList[i + 1], "occurs", countList[i + 1], end = "")
	if countList[i] == countList[i + 1]:
		print(", so they are balanced")
	else:
		print(", so they are not balanced", end = "")
		if countList[i] > countList[i + 1]:
			print("there are ", countList[i] - countList[i + 1], "more", sList[i], "than", sList[i + 1])
		else:
			print("; there are ", countList[i + 1] - countList[i], "more", sList[i + 1], "than", sList[i])
print("")


#(
lb0 = []
#)
rb0 = []
#[
lb1 = []
#]
rb1 = []
#{
lb2 = []
#}
rb2 = []
#<
lb3 = []
#>
rb3 = []
#collectionList
collectionList = [lb0, rb0, lb1, rb1, lb2, rb2, lb3, rb3]

with open(readFile, "r") as reader:
	lineCount = -1
	for line in reader:
		lineCount += 1 #count each line for indexing
		cCount = -1
		for c in line:
			cCount += 1 #count each character for indexing
			for i in range(0, len(sList), 1):
				if c == sList[i]:
					collectionList[i].append(str(lineCount) + str(cCount)) #index each occurance with a UID

#Overview of balance
print("This section gives an overview of the balance of brackets in", readFile)
for r in range(0, len(sList), 2):
	leftLength = len(collectionList[r])
	rightLength = len(collectionList[r + 1])
	print("There are", str(leftLength), sList[r], "and", str(rightLength) , sList[r], end = ", so ")
	if leftLength < rightLength:
		print("there are", str(rightLength - leftLength), "more", sList[r + 1], "than", sList[r])
	else:
		print("there are", str(leftLength - rightLength), "more", sList[r], "than", sList[r + 1])
print("")

#location of bad guys
print("This section identifies the position of illegal brackets in", readFile, "(it will be empty if there are no illegal brackets)")
for r in range(1, len(sList), 2):
	rightLocation = 0
	leftLocation = 0
	rightList = collectionList[r]
	leftList = collectionList[r - 1]
	rightLength = len(rightList)
	leftLength = len(leftList)
	if rightLength == 0:
		for i in leftList:
			print("Illegal", sList[r - 1], "at line", str(i[0]), ", position", str(i[1::]))
	elif leftLength == 0:
		for i in rightList:
			print("Illegal", sList[r], "at line", str(i[0]), ", position", str(i[1::]))
	else:
		while leftLocation < len(leftList) and rightLocation < len(rightList):
			if leftList[leftLocation] < rightList[rightLocation]:
				leftLocation += 1
				rightLocation += 1
			else:
				print("Illegal", sList[r], "at line", str(rightList[rightLocation][0]), ", position", str(rightList[rightLocation][1::]))
				rightLocation += 1
		for i in range(leftLocation, len(leftList), 1):
			print("Illegal", sList[r - 1], "at line", str(leftList[leftLocation][0]), ", position", str(leftList[leftLocation][1::]))
		for i in range(rightLocation, len(rightList), 1):
			print("Illegal", sList[r], "at line", str(rightList[rightLocation][0]), ", position", str(rightList[rightLocation][1::]))
print("")