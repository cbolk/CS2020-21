import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

neurons = []
val = float(raw_input())
while val != 0:
	neurons.append(val)
	val = float(raw_input())

print(neurons)

numneurons = len(neurons)
minlength = min(neurons)
maxlength = max(neurons)
avglength = float(sum(neurons)) / numneurons


neurons.sort()

middle = numneurons / 2		# numneurons // 2  in python 3
th25 = numneurons / 4		# ...
th75 = numneurons * 3 / 4	# ...
q2 = neurons[middle]
q1 = neurons[th25]
q3 = neurons[th75]

print(str(minlength), str(maxlength), str(avglength))
print(str(q1), str(q2), str(q3))
## visualization only
df = pd.DataFrame(neurons,columns=['Length'])
myfmcolor = sns.color_palette(['#4695d6','#fa6e57','#7ebc59','#fed95c'])
sns.set_palette(myfmcolor)
sns.boxplot(y='Length', data=df)
sns.swarmplot(y="Length", data=df, color=".25")
plt.show()