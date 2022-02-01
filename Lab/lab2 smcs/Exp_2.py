from scipy.stats import poisson
X = [0, 1, 2, 3]
miu = 5
poisson_pd = poisson.pmf(X, miu)
b= sum(poisson_pd)
print(b)



