from scipy.stats import binom
# setting the values
# of n and p
n = 10
p = 0.8
# defining the list of r values
r_values = list(range(n + 1))
# obtaining the mean and variance
mean, var = binom.stats(n, p)
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# printing the table
print("r\tp(r)")
for i in range(n + 1):
	print(str(r_values[i]) + "\t" + str(dist[i]))
# printing mean and variance
print("mean = "+str(mean))
print("variance = "+str(var))

import matplotlib.pyplot as plt
plt.bar(r_values, dist)
plt.show


