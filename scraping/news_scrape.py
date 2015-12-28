import requests
import re
from bs4 import BeautifulSoup
import simplejson as json
import urllib

def news_scrape(company):
	#takes in string variable of company

	weblist = ["http://www.anandtech.com/", "http://www.theverge.com/", "https://news.ycombinator.com/", 
		"http://arstechnica.com/", "http://www.pcgamer.com/hardware/", "http://www.tomshardware.com/",
		"http://www.techradar.com/us/pro"]

	total = 0
	count = 0

	for w in weblist:
		r = urllib.urlopen(w).read()
		soup = BeautifulSoup(r, "lxml")
		data = soup.findAll(text=True)
		text = filter(visible,data)
		text = str(text)
		text = re.sub("[^\w]", " ",  text).split()

		for x in text:
			total = total + 1
			if x.lower() == company:
				count = count + 1

	return count


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True