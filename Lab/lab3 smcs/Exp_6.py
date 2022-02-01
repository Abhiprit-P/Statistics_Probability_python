from scipy.stats import hypergeom

M = 30
n=5
N=14


mean, var = hypergeom.stats(M, n, N)


import matplotlib.pyplot as plt

for x in range(1,n+1):
    a= hypergeom.pmf(x,M, n, N)
    print(a)
    
plt.plot(x,a)   
plt.show()