import pandas as pd 
import numpy as np

path = "C:\\Users\\Admin\\Desktop\\student_scores.csv"

df = pd.read_csv(path)


a = df['Math']
b = df['Physics']
c = df['Chemistry']
d = df['English']

m1 = np.mean(a)
m2 = np.mean(b)
m3 = np.mean(c)
m4 = np.mean(d)


print('Average mark for college A: {}'.format(m1))
print('Average mark for college B: {}'.format(m2))
print('Average mark for college C: {}'.format(m3))
print('Average mark for college C: {}'.format(m4))


import scipy.stats as stats

stat, p=stats.f_oneway(a,b,c,d)
print('P value:', p)
if p > 0.05:
 print('Means are not different')
else:
 print('Means are different')




