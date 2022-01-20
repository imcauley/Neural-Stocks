import os

#used to delete data outside of time range

filepath = "/Users/marcojanker/development/Neural-Stocks/data/"
files = ["al", "cu", "gas", "eur", "gbp", "cny"]

time = open(os.path.join(filepath, "time.json"), "r")
time = time.read() 
time = eval(time)

date = open(os.path.join(filepath, "time.json"), "r")
date = date.read() 
date = eval(date)

count = 0

for f in files:
	openfile = open(os.path.join(filepath, f + ".json"), "r")
	openfile = openfile.read() 
	openfile = eval(openfile)

	floatarray = openfile[:-101]

	floatarray = str(floatarray)
	
	writefile = open(os.path.join(filepath, f + ".json"), "w")
	writefile.write(floatarray)