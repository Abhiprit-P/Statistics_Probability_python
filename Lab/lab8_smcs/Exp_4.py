import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import ztest as ztest

path = "C:\\Users\\Admin\\Downloads\\school.csv"
height = pd.read_csv(path)
print(height)

boys1 = height['Boys1'].tolist()
girls1 = height['Girls1'].tolist()

print(boys1)
print(girls1)

height_mean_boys = np.mean(height.Boys1)
print(height_mean_boys)

height_mean_girl1 = np.mean(height.Girls1)
print(height_mean_girl1)


zscore ,pval=ztest(boys1, girls1, value=0)
print(float(pval))
if pval<0.05:
 print("reject null hypothesis")
else:
 print("accept null hypothesis")
