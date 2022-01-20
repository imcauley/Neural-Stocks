from collections import Counter
import os

#used to see what dates have full data

filepath = "/Users/marcojanker/development/Neural-Stocks/data/"

date = open(os.path.join(filepath, "date.json"), "r")
date = date.read() 
date = eval(date)

print Counter(date)