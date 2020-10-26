day = int(raw_input())
month = int(raw_input())
year = int(raw_input())

if month >= 1 and month <= 12:
    numday = day  #add the day itself
    if month > 11:
        numday = numday + 30 #november days
    if month > 10:
        numday = numday + 31 #october days
    if month > 9:
        numday = numday + 30 #september days
    if month > 8:
        numday = numday + 31 
    if month > 7:
        numday = numday + 31 
    if month > 6:
        numday = numday + 30 
    if month > 5:
        numday = numday + 31 
    if month > 4:
        numday = numday + 30 
    if month > 3:
        numday = numday + 31 
    if month > 2:
        numday = numday + 28
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            numday = numday +1
    if month > 1:
        numday = numday + 31 
else:
    numday = -1
