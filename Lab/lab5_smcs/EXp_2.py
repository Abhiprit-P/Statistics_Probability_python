from scipy.stats import norm

x =25

a =  norm.cdf(x,loc=20,scale=1.5)

result = 1- a

print(result)

