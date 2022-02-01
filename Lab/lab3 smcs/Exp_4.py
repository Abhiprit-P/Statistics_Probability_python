from scipy.stats import hypergeom
import scipy.stats as ss
M = 20
n=5
N=6
k=4
hpd = ss.hypergeom(M, n, N)
p = hpd.pmf(k)
print(p)