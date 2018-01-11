from collections import Counter
import os

#used to see what dates have full data

filepath = "/home/isaac/Desktop/NeuralStocksMaster/data/"

date = open(os.path.join(filepath, "date.json"), "r")
date = date.read() 
date = eval(date)

print Counter(date)