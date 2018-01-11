import requests
import re
from bs4 import BeautifulSoup

def aluminium_scrape():
	r = requests.get("http://www.indexmundi.com/commodities/?commodity=aluminum")
	soup = BeautifulSoup(r.text, "lxml")
	future = soup.find('div', id="futuresPanel")
	array = []
	total = 0
	for child in future.children:
		array.append(child)

	al = array[3].text
	al = al.replace(",", "")
	al = float(al)
	al = al/3070
	al = round(al, 4)

	return al

def gas_scrape():
	r = requests.get("http://www.indexmundi.com/commodities/?commodity=natural-gas")
	soup = BeautifulSoup(r.text, "lxml")
	future = soup.find('div', id="futuresPanel")
	array = []
	total = 0
	for child in future.children:
		array.append(child)

	gas = array[3].text
	gas = gas.replace(",", "")
	gas = float(gas)
	gas = gas/5.98
	gas = round(gas, 4)

	return gas

def copper_scrape():
	r = requests.get("http://www.indexmundi.com/commodities/?commodity=copper")
	soup = BeautifulSoup(r.text, "lxml")
	future = soup.find('div', id="futuresPanel")
	array = []
	for child in future.children:
		array.append(child)

	cu = array[3].text
	cu = cu.replace(",", "")
	cu = float(cu)
	cu = cu/9880
	cu = round(cu, 4)
	
	return cu
