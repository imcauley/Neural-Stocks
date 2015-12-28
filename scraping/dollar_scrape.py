import requests
import re
from bs4 import BeautifulSoup
import simplejson as json

def eur_scrape():
	r = requests.get("http://www.xe.com/currency/usd-us-dollar")
	soup = BeautifulSoup(r.text, "lxml")

	eur = soup.find('a', rel="EUR,USD,1,1")
	eur = float(eur.text)

	return eur

def gbp_scrape():
	r = requests.get("http://www.xe.com/currency/usd-us-dollar")
	soup = BeautifulSoup(r.text, "lxml")

	gbp = soup.find('a', rel="GBP,USD,1,2")
	gbp = float(gbp.text)

	return gbp

def cny_scrape():
	r = requests.get("http://www.xe.com/currency/usd-us-dollar")
	soup = BeautifulSoup(r.text, "lxml")

	cny = soup.find('a', rel="CNY,USD,1,6")
	cny = float(cny.text)

	return cny