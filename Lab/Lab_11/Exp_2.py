import pandas as pd 
import numpy as np

path = "C:\\Users\\Admin\\Desktop\\salary_data.csv"

df = pd.read_csv(path)


a = df.loc[df['Company'] == 'TCS']
b = df.loc[df['Company'] == 'Infosys']
c = df.loc[df['Company'] == 'Wipro']

m1 = np.mean(a['Salary'])
m2 = np.mean(b['Salary'])
m3 = np.mean(c['Salary'])


print('Average mark for college A: {}'.format(m1))
print('Average mark for college B: {}'.format(m2))
print('Average mark for college C: {}'.format(m3))

import scipy.stats as stats

stat, p=stats.f_oneway(a['Salary'],b['Salary'],c['Salary'])

print('P value:', p)

if p > 0.05:

  print('Means are not different')

else:

  print('Means are different')
  
  