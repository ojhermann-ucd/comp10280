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

#screen output
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