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

#these are the first time instant with a temperature reading and the last one
firstreading = df.min().ts  # 2016-12-01 00:00
lastreading = df.max().ts   # 2017-01-31 23:30

datediff = lastreading - firstreading
if datediff.seconds == 0:
    ndays = datediff.days
else:
    ndays = datediff.days + 1

# create a skeleton with 1 sample every 30 minutes

#create a list of values from firstreading to lastreading, with 30mins of difference
# ts_list = [firstreading]
# nextday = firstreading + datetime.timedelta(0,30*60)  0 days, 30*60 seconds
# while nextday < lastreading:
# 	ts_list.append(nextday)
# 	nextday = firstreading + datetime.timedelta(0,30*60)  0 days, 30*60 seconds

# alternative 'easy' way
ts_list = pd.date_range(firstreading, lastreading, freq='30min')

#create a new df with these timestamps
ds = pd.DataFrame(ts_list, columns=['ts'])

#create a new column for the temperature - initialized to NaN
ds['temperature'] = np.nan

#copy the temperature without worrying about missing values ....
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

#compute the daily average temperature KEEPING IN MIND THAT THERE MIGHT BE MISSING VALUES
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

# #compute the daily average temperature KEEPING IN MIND THAT THERE MIGHT BE MISSING VALUES
# #alternative version using the computation of an average over a dataframe slice
# #more complex from the point of view of the syntax ...
# ds['average_daily_alt'] = np.nan
# day = firstreading.date()     # day = 2016-12-01
# lastday = lastreading.date()  # lastday = 2017-01-31
# while day <= lastday:
#     # filter data where the date is the one we want
#     # day is 2016-12-01
#     # the daily temperature readings are:
#     # I select the slice of rows I am interested .. the ones for day
#     nextday = day + datetime.timedelta(days=1)
#     # ts stores datetime .. to compare with datetime pd.Timestamp(day) 
#     dailytemps = ds[(ds['ts'] >= pd.Timestamp(day)) & (ds['ts'] < pd.Timestamp(nextday))]
# 	# I sliced the dataframe, 
# 	# I use the .mean() function to compute the average temperature
#     avgday = dailytemps.temperature.mean()
# 	# I update ALL rows of the day in the average_daily, with the computed average
#     ds.loc[(ds['ts'] >= pd.Timestamp(day)) & (ds['ts'] < pd.Timestamp(nextday)),'average_daily_alt'] = avgday
#     day = day + datetime.timedelta(days=1)

# # compare the two column values to see if there are mistakes in  
# # one of the algorithms
# ds[ds['average_daily'] <> ds['average_daily_alt']]
# # or plot to compare visually
# sns.lineplot(x="ts", y="average_daily", data=ds).set_title('Temperature')
# sns.lineplot(x="ts", y="average_daily_alt", data=ds).set_title('Temperature')
# plt.title("average_daily vs average_daily_alt", size=24)
# plt.show()
# plt.close()

# ## you should have only one column, no matter how you computed 

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
	step += 1

# # using built in features
# # 
# ds['average_24hrs_alt'] = np.nan
# for i in range(SAMPLESPERDAY, laststep):
#     rows = ds.loc[i-SAMPLESPERDAY:i-1, ['temperature']]
#     avgday = rows.temperature.mean()
#     ds.at[i,'average_24hrs_alt'] = avgday

# # compare the two column values to see if there are mistakes in  
# # one of the algorithms
# ds[ds['average_24hrs'] <> ds['average_24hrs_alt']]
# # or plot to compare visually
# sns.lineplot(x="ts", y="average_24hrs", data=ds)
# sns.lineplot(x="ts", y="average_24hrs_alt", data=ds).set_title('Temperature')
# plt.title("average_24hrs vs average_24hrs_alt", size=24)
# plt.show()
# plt.close()

#make sure you remove extra columns
ds = ds[['ts','temperature','average_daily','average_24hrs']]

## MATPLOTLIB PLOT
# make ts the index of the dataframe, which leads to timeseries plotting 
# with matplotlib
ds.set_index('ts').plot()
plt.xlabel("Date",size=10)
plt.ylabel("Temperature ($^\circ$C)",size=10)
plt.title("Laboratory Temperature Monitoring (matplotlib)", size=14)
plt.show()

## SEABORN PLOT
# one per column to be visualized -- the dataframe is not well organized
# note that the label on the y axis is the one of the LAST plot
plt.figure(figsize=(10, 6))
sns.lineplot(x="ts", y="temperature", data=ds)
sns.lineplot(x="ts", y="average_daily", data=ds)
sns.lineplot(x="ts", y="average_24hrs", data=ds)
plt.title("Laboratory Temperature Monitoring (seaborn not tidy df)", size=24)
plt.show()
plt.close()

## SEABORN PLOT
# one per column to be visualized -- the dataframe is not well organized
# customize a bit the plot

plt.figure(figsize=(10, 6))
sns.lineplot(x="ts", y="temperature", data=ds)
sns.lineplot(x="ts", y="average_daily", data=ds)
g = sns.lineplot(x="ts", y="average_24hrs", data=ds)
(g.set(ylabel="Temperature ($^\circ$C)", xlabel="Date"))
# we are customizing the last plot ... but it will seem applied to all
plt.title("Laboratory Temperature Monitoring 2 (seaborn not tidy df)", size=24)
plt.xticks(
     rotation=45, 
     horizontalalignment='right',
     fontweight='light',
     fontsize='small'  
)
plt.show()
plt.close()

# this is not a tidy dataframe ... it is difficult to plot 
# everything together ...
# let us make the df easy to plot now that it is prepared
#
dsplot = pd.melt(ds, id_vars=['ts'])
dsplot = dsplot.rename(columns={'variable':'type'})
dsplot.set_index('ts')
# print(dsplot)   #uncomment to see how data has been reorganized

plt.figure(figsize=(10, 6))
#g = sns.lineplot(x="ts", y="value", data=dsplot)
g = sns.lineplot(data=dsplot, x="ts", y="value", hue="type")
(g.set(ylabel="Temperature ($^\circ$C)", xlabel="Date"))
plt.title("Laboratory Temperature Monitoring", size=14)
plt.show()
plt.close()


## EXTRA FIX CHART DETAILS

#fix x axis labels
plt.figure(figsize=(10, 6))
#g = sns.lineplot(x="ts", y="value", data=dsplot)
g = sns.lineplot(data=dsplot, x="ts", y="value", hue="type")
(g.set(ylabel="Temperature ($^\circ$C)", xlabel="Date") .set_xticklabels(labels=x_dates, rotation=45, ha='right', fontsize='small'))
# or to rotate labels
# plt.xticks(
#     rotation=45, 
#     horizontalalignment='right',
#     fontweight='light',
#     fontsize='small'  
# )
plt.title("Laboratory Temperature Monitoring", size=14)
plt.show()
plt.close()



