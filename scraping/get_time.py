import datetime
from datetime import date

def get_time(): 
	now = datetime.datetime.now()
	minute = (now.minute *1.666666)/100
	time = now.hour+minute
	time = time/24

	return round(time, 4)

def get_date():
	start = date(2015, 12, 31)
	now = date.today()
	delta = now - start
	delta = delta.days
	delta = delta/float(365.000)
	delta = round(delta, 3)
	return delta