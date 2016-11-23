"""
Pseudocode
"""
import sys
import os
import datetime

#list of strings to find in the document
sList = ["<", ">", "e", "<!--", "-->", "new lines"]
countList = [0, 0, 0, 0, 0, 0] #i would have liked ot use a dictionary

#files
readFile = "p18p6read.txt"
recordFile = "p18p6record.txt"

#existence variables
readExist = os.path.isfile(readFile)
recordExist = os.path.isfile(recordFile)

#existence checks
if not readExist:
	print(readFile, "does not exists.")
	sys.exit()
if not recordExist:
	recordFile = open("p18p6record.txt", "w")
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
		
		for line in reader:
			countList[5] += 1 #count new lines
			for i in sList:
				countList[sList.index(i)] += line.count(i)

with open(recordFile, "a+") as writer:
	for i in range(0, len(sList), 1):
		writer.write(str(sList[i])) #show character of interest; using str() in case future list contains non-string characters
		writer.write(" occurs ")
		writer.write(str(countList[i])) #show count of character of interest
		writer.write(" times.")
		writer.write("\n")
	writer.write("\n")