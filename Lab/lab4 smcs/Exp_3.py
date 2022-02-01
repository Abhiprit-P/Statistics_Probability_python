from scipy.stats import norm

mean,sd = 175,10
f=205



a =norm.sf(f, mean, sd)

print(a)

print('result =', a * 330000)

