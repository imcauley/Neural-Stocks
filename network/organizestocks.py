import os
import numpy as np

filepath = "/Users/marcojanker/development/Neural-Stocks/data/"

openfile = open(os.path.join(filepath, "intelstock.json"), "r")
openfile = openfile.read() 
openfile = eval(openfile)

date = open(os.path.join(filepath, "date.json"), "r")
date = date.read() 
date = eval(date)


currentarray = []
count = 0

for x in openfile:
	if count % 36 == 0:
		print (date[count]) , ": ", currentarray
		print ""
		currentarray = []
	currentarray.append(x)
	count = count + 1