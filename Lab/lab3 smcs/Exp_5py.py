from scipy.stats import hypergeom
import scipy.stats as ss
M = 196
n=10
N=101
k=7
hpd = ss.hypergeom(M, n, N)
p = hpd.pmf(k)
print(p)

