import pandas as pd
import sys
import matplotlib.pyplot as mp

df = pd.read_csv('sobar-72.csv')

#df.plot()
#df.plot.barh(stacked=True);
#mp.show()
df.corr()
print(df.corr())
#mp.savefig(sys.stdout.buffer)
sys.stdout.flush()
sys.stdout.flush()
