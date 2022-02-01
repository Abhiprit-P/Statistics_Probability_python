from scipy.stats import geom
X = 5
p = 0.3
geom_pd = geom.pmf(X, p)
print(geom_pd)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)
y = geom.pmf(x, p=0.3)
plt.plot(x, y)
plt.show()

x = np.arange(0, 10, 1)
y = geom.cdf(x, p=0.3)
plt.plot(x, y)
plt.show()