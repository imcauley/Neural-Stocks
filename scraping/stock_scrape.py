import requests
import re
from bs4 import BeautifulSoup
import simplejson as json

def stock_scrape(stockid):

	r = requests.get("https://ca.finance.yahoo.com/q?s=" + stockid)
	soup = BeautifulSoup(r.text, "lxml")

	stock = soup.find('span', id="yfs_l84_" + stockid.lower())
	stock = stock.text
	stock = float(stock)
	stock = stock/50
	stock = round(stock,4)

	return stock