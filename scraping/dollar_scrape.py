import requests
import re
from bs4 import BeautifulSoup
import simplejson as json

def eur_scrape():
	r = requests.get("https://ca.finance.yahoo.com/q?s=EURUSD=X")
	soup = BeautifulSoup(r.text, "lxml")

	eur = soup.find("span", id="yfs_l10_eurusd=x")
	eur = float(eur.text)
	eur = eur/1.16

	return round(eur, 4)

def gbp_scrape():
	r = requests.get("https://ca.finance.yahoo.com/echarts?s=USDGBP=X")
	soup = BeautifulSoup(r.text, "lxml")

	gbp = soup.find("span", id="yfs_l10_usdgbp=x")
	gbp = float(gbp.text)

	return round(gbp, 4)

def cny_scrape():
	r = requests.get("https://ca.finance.yahoo.com/q?s=USDCNY=X")
	soup = BeautifulSoup(r.text, "lxml")

	cny = soup.find("span", id="yfs_l10_usdcny=x")
	cny = float(cny.text)
	cny = cny/6.8

	return round(cny, 4)