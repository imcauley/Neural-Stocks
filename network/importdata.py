import numpy as np
import os

filepath = "/home/isaac/Desktop/NeuralStocksMaster/data/"
files = ["date", "time", "intelstock", "amdstock", "nvdastock", "intelnews", "amdnews", "nvdanews", "al", "cu", "gas", "eur", "gbp", "cny"]


datefile = open(os.path.join(filepath, "date.json"), "r")
datefile = datefile.read() 
datefile = eval(datefile)

dates = np.array([datefile])
dates = np.unique(dates)
totaldates = np.unique(dates).size

def indata(days):
	fulldata = np.array([], dtype=float)
	fulldata = np.empty([1,((totaldates - days) * 36)]) #make empty array
	for x in files: #open each file
		openfile = open(os.path.join(filepath, x + ".json"), "r")
		openfile = openfile.read() 
		openfile = eval(openfile)
		newdata = np.delete(openfile, np.s_[((totaldates - days) * 36):])

		fulldata = np.vstack((fulldata, newdata)) #put open file in 2D array

	#coverting array
	fulldata = np.delete(fulldata, 0, 0)
	fulldata = np.swapaxes(fulldata, 0, 1)
	return fulldata

def outdata(days):
	openfile = open(os.path.join(filepath, "intelstock.json"), "r")
	openfile = openfile.read() 
	openfile = eval(openfile)
	newdata = np.array([openfile])
	newdata = np.delete(openfile, np.s_[:(days*36)])
	newdata.shape += (1,)
	return newdata

def todaydata():
	fulldata = np.array([], dtype=float)
	fulldata = np.empty([1,36])
	for x in files:
		openfile = open(os.path.join(filepath, x + ".json"), "r")
		openfile = openfile.read() 
		openfile = eval(openfile)
		newdata = np.delete(openfile, np.s_[:((totaldates - 1) * 36)])
		fulldata = np.vstack((fulldata, newdata))

	fulldata = np.delete(fulldata, 0, 0)
	fulldata = np.swapaxes(fulldata, 0, 1)
	return fulldata

def fullindata():
	fulldata = np.array([], dtype=float)
	fulldata = np.empty([1,540]) #make empty array

	date = open(os.path.join(filepath, "date.json"), "r")
	date = date.read() 
	date = eval(date)

	days = [0.211, 0.214, 0.222, 0.225, 0.227, 0.230, 0.241, 0.247, 0.249, 0.252, 0.279, 0.282, 0.285, 0.288, 0.290]

	correctdays = []
	count = 0
	for x in date:
		if x in days:
			correctdays.append(count)
		count = count + 1

	for x in files: #open each file
		newdata = []
		openfile = open(os.path.join(filepath, x + ".json"), "r")
		openfile = openfile.read() 
		openfile = eval(openfile)

		for day in correctdays:
			newdata.append(openfile[day])

		fulldata = np.vstack((fulldata, newdata)) #put open file in 2D array

	#coverting array
	fulldata = np.delete(fulldata, 0, 0)
	fulldata = np.swapaxes(fulldata, 0, 1)
	return fulldata

def fulloutdata():
	date = open(os.path.join(filepath, "date.json"), "r")
	date = date.read() 
	date = eval(date)
	
	days = [0.214, 0.222, 0.225, 0.227, 0.230, 0.241, 0.247, 0.249, 0.252, 0.279, 0.282, 0.285, 0.288, 0.290, 0.299]

	correctdays = []
	count = 0
	for x in date:
		if x in days:
			correctdays.append(count)
		count = count + 1

	newdata = []
	openfile = open(os.path.join(filepath, "intelstock.json"), "r")
	openfile = openfile.read() 
	openfile = eval(openfile)

	for day in correctdays:
		newdata.append(openfile[day])

	return newdata