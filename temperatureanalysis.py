# Write a program that gets temperature readings for an ambient for scientific experiments
# for Dec. 2016 and Jan. 2017, sampled every 30 minutes, except for anomalies from the 
# sensors or the software, such that there might be missing samples, or redundant ones.
# The program prepares the data, by cleaning it (remove duplicates and fills missing data)
# and then plots it.
# To get an idea of the temperature trend, we also want to compute the average 
# temperature for the day, and plot it.
# Finally, we want to use a moving average window on 24 hours to sample the temperature and
# plot it to compare it against the nominal temperature.

# Steps
#
# Load csv data into dataframes 
#
# Create a single dataframe with information from both months
# (either concatenate the files, by creating a single file, or concatenate dataframes)
#
# Prepare a skelethon for having 1 reading every 30 minutes
# + generate a timestamp from minumum to maximum
# + work with timestamp variables
#
# Fill each timestamp with 1 value - if more are available, compute and use the mean
#
# Plot it (with missing values)
#
# Compute the average temperature for each day
# 
# Plot it together with the temperature
#
# Identify problems with missing values, and solve it
#
#

import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

SAMPLESPERDAY = 24 * 2

df2016 = pd.read_csv("~/cs/classes/201612.csv")
df2017 = pd.read_csv("~/cs/classes/201701.csv")

df = pd.concat([df2016, df2017])
df['ts'] = (df.date) + ' ' + (df.time)
df.ts = df.ts.apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%y %H:%M:%S'))
df = df[['ts', 'temperature']]
# create a skeleton with 1 sample every 30 minutes
firstday = df.min().ts
lastday = df.max().ts

datediff = lastday - firstday
if datediff.seconds == 0:
    ndays = datediff.days
else:
    ndays = datediff.days + 1


#create a list of values from firstday to lastday, with 30mins of difference
# ts_list = [firstday]
# nextday = firstday + datetime.timedelta(0,30*60)  0 days, 30*60 seconds
# while nextday < lastday:
# 	ts_list.append(nextday)
# 	nextday = firstday + datetime.timedelta(0,30*60)  0 days, 30*60 seconds

# alternative 'easy' way
ts_list = pd.date_range(firstday, lastday, freq='30min')

#create a new df with these timestamps
ds = pd.DataFrame(ts_list, columns=['ts'])

#create a new column for the temperature - initialized to NaN
ds['temperature'] = np.nan

#copy the temperature
nrows = len(ds)
for i in range(0, nrows):
    rows = df.loc[df.ts == ds.iloc[i].ts, ['temperature']]
    nreadings = len(rows)
    if nreadings == 1:     #if there is one readings, take it
        ds.at[i,'temperature'] = rows.iloc[0].temperature
    elif nreadings > 1:   #too many readings
        ds.at[i,'temperature'] = rows.temperature.mean()



#let us see if there are NaN in the data
if len(ds[ds.temperature.isna() == True]):
	print("there are missing values")

#compute the daily average temperature
ds['average_daily'] = np.nan
day = 0
while day < ndays:
	tot = 0.0
	dec = 0
	for iv in range(0, SAMPLESPERDAY):
		t = ds.iloc[day*SAMPLESPERDAY + iv, 1]
		if pd.isna(t):
			dec += 1 #decrement the number of samples
		else:
			tot += t
	avgday = tot/(SAMPLESPERDAY - dec)
	for iv in range(0, SAMPLESPERDAY):
		ds.at[day*SAMPLESPERDAY + iv, 'average_daily'] = avgday
	day += 1

#compute the moving average over 24 hours
ds['average_24hrs'] = np.nan
step = SAMPLESPERDAY
laststep = ndays * SAMPLESPERDAY
while step < laststep:
	tot = 0.0
	dec = 0
	for iv in range(step-SAMPLESPERDAY, step):
		t = ds.iloc[iv, 1]
		if pd.isna(t):
			dec += 1 #decrement the number of samples
		else:
			tot += t
	avgday = tot/(SAMPLESPERDAY - dec)
	ds.at[step, 'average_24hrs'] = avgday
#	print('>>>', step, avgday)
	step += 1

#using built in features
ds['filtered_ma'] = np.nan
for i in range(SAMPLESPERDAY, laststep):
#    rows = ds.ix[i-SAMPLESPERDAY:i-1, ['temperature']]
    rows = ds.loc[i-SAMPLESPERDAY:i-1, ['temperature']]
    avgday = rows.temperature.mean()
#    print('>>>', i, avgday)
    ds.at[i,'filtered_ma'] = avgday

#print(ds)

#plot everything
plt.figure(figsize=(10, 6))
sns.lineplot(x="ts", y="temperature", data=ds)
sns.lineplot(x="ts", y="average_daily", data=ds).set_title('Temperature')
ax = sns.lineplot(x="ts", y="average_24hrs", data=ds).set_title('Temperature')
ax.set_xticklabels(rotation=90)
plt.show()
plt.close()




