# import required libraries
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
 
# Creating the distribution
data = np.arange(1,100,0.01)
pdf = norm.pdf(data , loc = 50 , scale = 15 )
 
#Visualizing the distribution
 
sb.set_style('whitegrid')
sb.lineplot(data, pdf , color = 'black')
plt.xlabel('Heights')
plt.ylabel('Probability Density')

cdf_upper_limit = norm(loc = 50 , scale = 15).cdf(70)
cdf_lower_limit = norm(loc = 50 , scale = 15).cdf(50)
 
prob = cdf_upper_limit - cdf_lower_limit
print(prob)

plt.fill_between(data, pdf, where =(data >50) & (data <70))
