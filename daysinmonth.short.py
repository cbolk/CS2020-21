
month = int(raw_input())
if month == 2:
	ndays = 28
elif month == 4 or \
	month == 6 or \
	month == 9 or \
	month == 11:
	ndays = 30
else:
	ndays = 31

