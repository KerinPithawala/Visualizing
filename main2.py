import pandas as pd
import matplotlib.pyplot  as mp



df = pd.read_csv('sobar-72.csv')

#df.plot('behavior_eating','attitude_consistency','attitude_spontaneity')
#scatter-plot for behaviour eating with cervix cancer
df.plot(kind = 'scatter', x = 'attitude_spontaneity', y = 'ca_cervix')

mp.show()