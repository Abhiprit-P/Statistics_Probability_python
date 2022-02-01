from scipy.stats import nbinom

p = 0.7 
n =3
x =5
mean, var = nbinom.stats(n, p)

a1= nbinom.pmf(x, n, p)

a2= nbinom.cdf(x, n, p)

print(a1)
print(a2)


