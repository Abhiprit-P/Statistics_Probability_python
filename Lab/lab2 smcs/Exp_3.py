#Exp_3
#a:
from math import factorial, exp
from scipy.stats import poisson

miu = 3
x = 0
poisson_prob = ((miu ** x) * exp(-miu)) / factorial(x)
result = 1- poisson_prob
print(result)

#b:
X = [2, 3, 4]
miu = 3
poisson_pd = poisson.pmf(X, miu)
b= sum(poisson_pd)
print(b)

#c:
X = 1
miu = 0.6
poisson_pd = poisson.pmf(X, miu)
print(poisson_pd)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10,1)
y = poisson.pmf(x, mu=3)
plt.plot(x, y)
plt.show()

x = np.arange(0, 10, 1)
y = poisson.cdf(x, mu=3)
plt.plot(x, y)
plt.show()

