import numpy as np
a=[210,240,270,270,300]
b=[210,240,240,270,270]
c=[180,210,210,210,210]
m1=np.mean(a)
m2=np.mean(b)
m3=np.mean(c)
print('Average mark for college A: {}'.format(m1))
print('Average mark for college B: {}'.format(m2))
print('Average mark for college C: {}'.format(m3))
import scipy.stats as stats
stat, p=stats.f_oneway(a,b,c)
print('P value:', p)
if p > 0.05:
 print('Alternative Hypothesis is true: Atleast Means are not different')
else:
 print('Null Hypothesis is true : Means are same')


