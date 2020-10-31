import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ADENINE = 'A'
CYTOSINE = 'C'
GUANINE = 'G'
THYMINE = 'T'

DNAELEM = ADENINE + CYTOSINE + GUANINE + THYMINE
nDNAElem = len(DNAELEM)

sequence = input()

elementlist = list(sequence)
#reverse operation
#seq = ''.join(elementlist)
#to have A C G T
elementlist.sort()


## visualization only
df = pd.DataFrame(elementlist,columns=['BASE'])
myfmcolor = sns.color_palette(['#4695d6','#fa6e57','#7ebc59','#fed95c'])
sns.set_palette(myfmcolor)
sns.displot(x='BASE', data=df, hue="BASE", shrink=.8)
plt.title('Sequence DNA bases')
plt.show()
