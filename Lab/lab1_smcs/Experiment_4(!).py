from scipy.stats import binom
# setting the values
# of n and p
n = 12
p = 0.2
# obtaining the mean and variance
mean, var = binom.stats(n, p)
# list of pmf values
dist = [binom.pmf(2, n, p)]
print("mean = "+str(mean))
print("variance = "+str(var))

print(binom.pmf(2, n, p))



