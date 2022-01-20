import os

#used to see how many data points each file has

filepath = "/Users/marcojanker/development/Neural-Stocks/data/"
files = ["date", "time", "intelstock", "amdstock", "nvdastock", "intelnews", "amdnews", "nvdanews", "al", "cu", "gas", "eur", "gbp", "cny"]

for f in files:
	openfile = open(os.path.join(filepath, f + ".json"), "r")
	openfile = openfile.read() 
	openfile = eval(openfile)

	num = 0

	for x in openfile:
		num = num + 1

	print num