import matplotlib.pyplot as plt
import os
import numpy as np

filepath = "/home/isaac/Desktop/NeuralStocksMaster/data/"
filepath2 = "/home/isaac/Desktop/NeuralStocksMaster/predictions/"

#open actual stock
openfile = open(os.path.join(filepath, "intelstock.json"), "r")
openfile = openfile.read() 
openfile = eval(openfile)

filename = "2016-03-27-1-30-2500-1"

#open predicted stock
prediction = open(os.path.join(filepath2, filename + ".json"), "r")
prediction = prediction.read() 
prediction = eval(prediction)


stock = np.delete(openfile, np.s_[:-36])
predictionarray = np.array(prediction)

#convert regulated data to actaul data
stock = stock * 50
predictionarray = predictionarray * 50


z = np.amax(predictionarray)
xcount = 0

#for x in predictionarray:
#	if x != z:
#		q = z - x
#		x2 = z + q#

#		predictionarray[xcount] = x2#

#	xcount = xcount + 1

error = (((stock - predictionarray) / stock) * 100) 

print np.mean(error)

#find delta
delta1 = stock[0] - stock[35]
print delta1

delta2 = predictionarray[0] - predictionarray[35]
print delta2

#graphing
plt.plot(stock)
plt.plot(predictionarray)
axes = plt.gca()
axes.set_ylim([20,35])
plt.ylabel('some numbers')
plt.show()