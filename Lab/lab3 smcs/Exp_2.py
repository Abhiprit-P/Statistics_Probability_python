from scipy.stats import nbinom

p = 0.2
n =5
x =10
mean, var = nbinom.stats(n, p)

a1= nbinom.pmf(x, n, p)
    
a2= nbinom.cdf(x, n, p)

print(a1)
print(a2)


