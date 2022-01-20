import stock_scrape as ss
import news_scrape as ns
import dollar_scrape as ds
import material_scrape as ms
import get_time as gt
import json
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

logging.basicConfig()

#array format: [time, stocks, news, dollar, material]

#main loop
def tick():
	checktime = gt.get_time()

	if 0.375 < checktime < 0.625: 

		filepath = "/Users/marcojanker/development/Neural-Stocks/data/"

		time = open(os.path.join(filepath, "time.json"), "a")
		time.write(", " + json.dumps(gt.get_time()))
		time.close

		date = open(os.path.join(filepath, "date.json"), "a")
		date.write(", " + json.dumps(gt.get_date()))
		date.close

		intelstock = open(os.path.join(filepath, "intelstock.json"), "a")
		intelstock.write(", " + json.dumps(ss.stock_scrape("INTC")))
		intelstock.close

		amdstock = open(os.path.join(filepath, "amdstock.json"), "a")
		amdstock.write(", " + json.dumps(ss.stock_scrape("AMD")))
		amdstock.close

		nvdastock = open(os.path.join(filepath, "nvdastock.json"), "a")
		nvdastock.write(", " + json.dumps(ss.stock_scrape("NVDA")))
		nvdastock.close

		intelnews = open(os.path.join(filepath, "intelnews.json"), "a")
		intelnews.write(", " + json.dumps(ns.news_scrape("intel")))
		intelnews.close

		amdnews = open(os.path.join(filepath, "amdnews.json"), "a")
		amdnews.write(", " + json.dumps(ns.news_scrape("amd")))
		amdnews.close

		nvdanews = open(os.path.join(filepath, "nvdanews.json"), "a")
		nvdanews.write(", " + json.dumps(ns.news_scrape("nvidia")))
		nvdanews.close

		eur = open(os.path.join(filepath, "eur.json"), "a")
		eur.write(", " + json.dumps(ds.eur_scrape()))
		eur.close

		gbp = open(os.path.join(filepath, "gbp.json"), "a")
		gbp.write(", " + json.dumps(ds.gbp_scrape()))
		gbp.close

		cny = open(os.path.join(filepath, "cny.json"), "a")
		cny.write(", " + json.dumps(ds.cny_scrape()))
		cny.close

		al = open(os.path.join(filepath, "al.json"), "a")
		al.write(", " + json.dumps(ms.aluminium_scrape()))
		al.close

		gas = open(os.path.join(filepath, "gas.json"), "a")
		gas.write(", " + json.dumps(ms.gas_scrape()))
		gas.close

		cu = open(os.path.join(filepath, "cu.json"), "a")
		cu.write(", " + json.dumps(ms.copper_scrape()))
		cu.close

		print gt.get_time()
		print ss.stock_scrape("INTC")
		print "---------------"
		
	else: 
		print "*"

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', minutes=10)
    #every 10 minutes

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass