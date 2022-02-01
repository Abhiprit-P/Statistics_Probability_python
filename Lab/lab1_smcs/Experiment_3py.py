from scipy.stats import binom
# setting the values
# of n and p
n = 10
p = 0.1
# defining the list of r values
r_values = [4,5,6,7,8,9,10]
# obtaining the mean and variance
mean, var = binom.stats(n, p)
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# printing the table
print("r\tp(r)")
for i in r_values:
	print(str(r_values[i]) + "\t" + str(dist[i]))
# printing mean and variance
print("mean = "+str(mean))
print("variance = "+str(var))

P_4 =(binom.pmf(4, n, p))
P_5 =(binom.pmf(5, n, p))
P_6 =(binom.pmf(6, n, p))
P_7 =(binom.pmf(7, n, p))
P_8 =(binom.pmf(8, n, p))
P_9 =(binom.pmf(9, n, p))
P_10 =(binom.pmf(10, n, p))

sum = P_4 + P_5 + P_6 + P_7 + P_8 + P_9 + P_10
result = 1- sum
print(result)
