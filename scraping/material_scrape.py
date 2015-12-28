import requests
import re
from bs4 import BeautifulSoup
import simplejson as json

def aluminium_scrape():
	r = requests.get("http://www.indexmundi.com/commodities/?commodity=aluminum")
	soup = BeautifulSoup(r.text, "lxml")
	future = soup.find('div', id="futuresPanel")
	array = []
	total = 0
	for child in future.children:
		array.append(child)

	al =  float(array[3].text)
	return al

def gas_scrape():
	r = requests.get("http://www.indexmundi.com/commodities/?commodity=natural-gas")
	soup = BeautifulSoup(r.text, "lxml")
	future = soup.find('div', id="futuresPanel")
	array = []
	total = 0
	for child in future.children:
		array.append(child)

	gas =  float(array[3].text)
	return gas

def copper_scrape():
	r = requests.get("http://www.indexmundi.com/commodities/?commodity=copper")
	soup = BeautifulSoup(r.text, "lxml")
	future = soup.find('div', id="futuresPanel")
	array = []
	total = 0
	for child in future.children:
		array.append(child)

	cu =  array[3].text
	''.join(c for c in cu if c.isdigit())
	cu = float(cu)
	
	return cu

def oil_scrape():
	r = requests.get("http://www.indexmundi.com/commodities/?commodity=crude-oil-brent")
	soup = BeautifulSoup(r.text, "lxml")
	future = soup.find('div', id="futuresPanel")
	array = []
	total = 0
	for child in future.children:
		array.append(child)

	oil =  float(array[3].text)
	return oil
