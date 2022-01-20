import matplotlib.pyplot as plt
import os

#used for graphing

filepath = "/Users/marcojanker/development/Neural-Stocks/data/"

openfile = open(os.path.join(filepath, "intelstock.json"), "r")
openfile = openfile.read() 
openfile = eval(openfile)

openfile = openfile

plt.plot(openfile)
plt.ylabel('Intel Stock')
plt.show()