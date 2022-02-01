from scipy.stats import norm

x,mean,sd = 13,4.4,1.3
f,g= 7.0,3.1



a =norm(mean, sd).cdf(f)
b =norm(mean, sd).cdf(g)

c = a -b
print('sum:', c)
