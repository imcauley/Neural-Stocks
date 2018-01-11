import os

#used to delete dates that dont have full data

filepath = "/home/isaac/Desktop/NeuralStocksMaster/data/"
files = ["date", "time", "intelstock", "amdstock", "nvdastock", "intelnews", "amdnews", "nvdanews", "al", "cu", "gas", "eur", "gbp", "cny"]

date = open(os.path.join(filepath, "date.json"), "r")
date = date.read() 
date = eval(date)

badnum = []
count = 0

for x in date:
	if x == 0.041: 
		badnum.append(count)
	count = count + 1

print badnum

for f in files:
	openfile = open(os.path.join(filepath, f + ".json"), "r")
	openfile = openfile.read() 
	openfile = eval(openfile)

	floatarray = []

	for e in openfile:
		floatarray.append(e)

	for n in reversed(badnum):
		del floatarray[n]

	floatarray = str(floatarray)
	
	writefile = open(os.path.join(filepath, f + ".json"), "w")
	writefile.write(floatarray)