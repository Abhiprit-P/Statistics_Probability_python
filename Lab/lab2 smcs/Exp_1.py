from math import factorial, exp

miu = float(input('enter the value of miu:'))
x = int(input('enter the value of x:'))
poisson_prob = ((miu ** x) * exp(-miu)) / factorial(x)
print(poisson_prob)



from scipy.stats import nbinom

mean, var = nbinom.stats(n, p)