import pandas as pd

df = pd.read_csv("./students.csv")

df.sort_values('mathematics')
df['rankM'] = df['mathematics'].rank()
meanrankm  = df['rankM'].mean()
df['rankM-m'] = df['rankM'] - meanrankm
df['rankM-m-sq'] = (df['rankM'] - meanrankm)*(df['rankM'] - meanrankm)
df['rankS'] = df['science'].rank()
meanranks  = df['rankS'].mean()
df['rankS-m'] = df['rankS'] - meanranks
df['rankS-m-sq'] = (df['rankS'] - meanranks)*(df['rankS'] - meanranks)

sumM = df['rankM-m-sq'].sum()
sumS = df['rankS-m-sq'].sum()

#df.corr(method='pearson')
#df.corr(method ='kendall')

df.corr(method ='spearman')
