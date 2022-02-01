from scipy.stats import binom
# setting the values
# of n and p
n = 8
p = 0.10
# defining the list of r values
# obtaining the mean and variance
mean, var = binom.stats(n, p)
# list of pmf values
dist = [binom.pmf(1, n, p)]
print("mean = "+str(mean))
print("variance = "+str(var))

print(binom.pmf(1, n, p))
