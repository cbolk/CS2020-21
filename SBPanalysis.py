import pandas as pd

TWOTAILED = 'TTT'
ONETAILED = 'OTT'

ALPHA05 = 0.05   
ALPHA01 = 0.05   

selalpha = ALPHA05
#selalpha = float(raw_input())

dfw = pd.read_csv("./WSRTdf.csv")

df = pd.read_csv("./SystolicBloodPressureAnalysis.csv")
number_of_samples = len(df)

df['Difference'] = df.SBP_before - df.SBP_after
df['AbsDiff'] = abs(df.Difference)
df = df.sort_values(['AbsDiff', 'Difference'])


df['Ranks'] = df['AbsDiff'].rank()
df['R+'] = df['Ranks']*(df['Difference'] > 0)
df['R-'] = df['Ranks']*(df['Difference'] < 0)

Wplus = sum(df['R+'])
Wminus = sum(df['R-'])

W = min(Wplus, Wminus)

#selecting the matching value in the table
threshold = dfw[(dfw['type'] == TWOTAILED) & (dfw['alpha'] == selalpha) & (dfw['n'] == number_of_samples)]['value'].iloc[0]

if W > threshold:
	print("Accepted")
else:
	print("Rejected")
	