import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

SAMPLEFREQ = 30 * 60   #30 minutes = 30 * 60 seconds
SAMPLEPERDAY = 24 * 2

df2016 = pd.read_csv("201612.csv")
df2017 = pd.read_csv("201701.csv")

df = pd.concat([df2016, df2017])
df['ts'] = (df.date) + ' ' + (df.time)
df.ts = df.ts.apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%y %H:%M:%S'))
df = df[['ts', 'temperature']]
#df.index = df.ts

fday = min(df.ts)
lday = max(df.ts)

#further information on the smapling windows
datediff = lday - fday

if datediff.seconds == 0:
    ndays = datediff.days
else:
    ndays = datediff.days + 1

## version 1
# ds = pd.DataFrame()
# ts = fday
# while (ts <= lday):
#     # ts is equal to 01/12/2016 00:00
#     rows = df.loc[df.timestamp == ts, ['temperature']]
#     nreadings = len(rows)
#     if nreadings == 1:     #if there is one readings, take it
#         ds = ds.append([[ts, rows.iloc[0].temperature]])
#     elif nreadings > 1:   #too many readings
#         ds = ds.append([[ts, rows.temperature.mean()]])
#     else: # no readings
#         ds = ds.append([[ts, np.nan]])
#     ts = ts + datetime.timedelta(0, SAMPLEFREQ)  #next timestamp
# ds = ds.rename(columns={0: "ts", 1: "temperature"})


ts_index = pd.date_range(fday, lday, freq='30min')
ds = pd.DataFrame(ts_index, columns=['ts'])
nrows = len(ds)
ds['temperature'] = np.nan
for i in range(0, nrows):
    rows = df.loc[df.ts == ds.iloc[i].ts, ['temperature']]
    nreadings = len(rows)
    if nreadings == 1:     #if there is one readings, take it
        ds.at[i,'temperature'] = rows.iloc[0].temperature
    elif nreadings > 1:   #too many readings
        ds.at[i,'temperature'] = rows.temperature.mean()


#ds = ds.rename(columns={0: "ts", 1: "temperature"})

ds['filtered'] = np.nan
day = 0
while day < ndays:
	totday = 0.0
	for iv in range(0, SAMPLEPERDAY):
		totday += ds.iloc[day*SAMPLEPERDAY + iv, 1]
	avgday = totday/SAMPLEPERDAY
	for iv in range(0, SAMPLEPERDAY):
		ds.at[day*SAMPLEPERDAY + iv, 'filtered'] = avgday
	day += 1


#if there are NaN, don't make mistakes
dst['filtered'] = np.nan
day = 0
while day < ndays:
	totday = 0.0
	dec = 0
	for iv in range(0, SAMPLEPERDAY):
		t = dst.iloc[day*SAMPLEPERDAY + iv, 1]
		if pd.isna(t):
			dec += 1 #decrement the number of samples
		else:
			totday += t
	avgday = totday/(SAMPLEPERDAY - dec)
	for iv in range(0, SAMPLEPERDAY):
		dst.at[day*SAMPLEPERDAY + iv, 'filtered'] = avgday
	day += 1

#moving average on 24 samples
dst['filtered_ma'] = np.nan
for i in range(SAMPLEPERDAY, nrows):
    rows = df.ix[i-SAMPLEPERDAY:i, ['temperature']]
    ds.at[i,'filtered_ma'] = rows.temperature.mean()



ds['day'] = ds['ts'].dt.day
ds['month'] = ds['ts'].dt.month
dst['dm'] = dst.ts.apply(lambda x: x.strftime('%d-%m')) 

ds['filtered_bi'] = ds.iloc[:,1].rolling(window=SAMPLEPERDAY).mean()

#ds['filtered_cum'] = ds.iloc[:,1].expanding(min_periods=SAMPLEPERDAY).mean()
#ds['filtered_exp'] = ds.iloc[:,1].ewm(span=SAMPLEPERDAY,adjust=False).mean()

#sns.lineplot(x="ts", y="temperature", data=ds)
#sns.lineplot(x="ts", y="filtered", data=ds)
#sns.lineplot(x="ts", y="filtered_bi", data=ds)
#sns.lineplot(x="ts", y="filtered_cum", data=ds)
#sns.lineplot(x="ts", y="filtered_exp", data=ds)
sns.boxplot(x="DM", y="temperature", hue="month", data=dst)
#plt.legend()
plt.show()
