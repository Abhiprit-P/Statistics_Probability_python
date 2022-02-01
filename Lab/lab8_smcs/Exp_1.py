from scipy.stats import ttest_1samp
import numpy as np
import pandas as pd

path = "C:\\Users\\Admin\\Downloads\\school.csv"
height = pd.read_csv(path)
print(height )
height_mean_boys = np.mean(height.Boys1)
print(height_mean_boys)
tset, pval = ttest_1samp(height.Boys1, 5.7)
print(pval)
if pval < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")
  
  
  

