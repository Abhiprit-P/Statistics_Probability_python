from scipy.stats import norm

x,mean,sd = 13,14,1
a =norm.sf(x ,mean,sd)
print(a)

