#Experiment_4 (2)


from scipy.stats import binom
# setting the values
# of n and p
n = 12
p = 0.2
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

P_0 =(binom.pmf(0, n, p))
P_1 =(binom.pmf(1, n, p))
P_2 =(binom.pmf(2, n, p))

result_1 = P_0 + P_1 + P_2
print(result_1)

#Experiment_4 (3)
result_2 = 1- result_1

print(result_2)
