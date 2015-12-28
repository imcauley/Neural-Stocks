import stock_scrape as ss
import news_scrape as ns
import dollar_scrape as ds
import material_scrape as ms
import datetime

#json object:
#object = [[time,stock, news, dollars, materials], [time,next stock,etc]

# array = [stock_scrape("INTC"),stock_scrape("AMD"), stock_scrape("NVDA"), news_scrape("intel"), news_scrape("amd"), news_scrape("nivida"), dollar_scrape()]

now = datetime.datetime.now()
time = now.hour + ((now.minute*1.67)/100)

array = [time, ss.stock_scrape("INTC"), ss.stock_scrape("AMD"), ss.stock_scrape("NVDA"), ns.news_scrape("intel"), ns.news_scrape("amd"), ns.news_scrape("nvidia"), ds.eur_scrape(), ds.gbp_scrape(), ds.cny_scrape(), ms.aluminium_scrape(), ms.gas_scrape(), ms.copper_scrape(), ms.oil_scrape()]

print array