import os

#used to delete data outside of time range

filepath = "/Users/marcojanker/development/Neural-Stocks/data/"
files = ["date", "time", "intelstock", "amdstock", "nvdastock", "intelnews", "amdnews", "nvdanews", "al", "cu", "gas", "eur", "gbp", "cny"]

time = open(os.path.join(filepath, "time.json"), "r")
time = time.read() 
time = eval(time)

date = open(os.path.join(filepath, "date.json"), "r")
date = date.read() 
date = eval(date)
print date

badnum = []
count = 0

for x in time:
	if date[count] > 0.226:
		if x < 0.375: 
			badnum.append(count)
		elif x >= 0.625:
			badnum.append(count)

	count = count + 1

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