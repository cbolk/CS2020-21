import numpy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


neurons = []
val = float(raw_input())
while val != 0:
	neurons.append(val)
	val = float(raw_input())

#debug printing
#print(neurons)

numneurons = len(neurons)
minlength = min(neurons)
maxlength = max(neurons)

avglength = numpy.mean(neurons)
stddev = numpy.std(neurons)
print(str(minlength), str(maxlength), str(avglength), str(stddev))

## visualization only
df = pd.DataFrame(neurons,columns=['Length'])
#myfmcolor = sns.color_palette(['#4695d6','#fa6e57','#7ebc59','#fed95c'])
#sns.set_palette(myfmcolor)
sns.boxplot(y='Length', data=df)
plt.show()
