# import required libraries
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
 
# Creating the distribution
data = np.arange(1,200,0.01)
pdf = norm.pdf(data , loc = 90 , scale = 10 )
 
#Visualizing the distribution
 
sb.set_style('whitegrid')
sb.lineplot(data, pdf , color = 'black')
plt.xlabel('Heights')
plt.ylabel('Probability Density')

cdf_value = norm(loc = 90 , scale = 10).cdf(100)

 
prob = 1- cdf_value
print(prob)

plt.fill_between(data, pdf, where =(data >100))

