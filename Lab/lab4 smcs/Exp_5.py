import numpy as np
import matplotlib.pyplot as plt
 

mean , sd = 80,5.2
a,b= mean -3*sd,mean +3*sd
x = np.linspace(a,b,200)


def normal_dist(x , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density
 
#Calculate mean and Standard deviation.
#mean = np.mean(x)
#sd = np.std(x)
 
#Apply function to the data.
pdf = normal_dist(x,mean,sd)
 
#Plotting the Results
plt.plot(x,pdf)
plt.xlabel('Data points')
plt.ylabel('Probability Density')



