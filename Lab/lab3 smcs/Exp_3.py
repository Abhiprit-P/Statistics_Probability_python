from scipy.stats import nbinom

p = 0.42 
n =4
x =14
mean, var = nbinom.stats(n, p)

a1= nbinom.pmf(x, n, p)

a2= nbinom.cdf(x, n, p)

print(a1)
print(a2)