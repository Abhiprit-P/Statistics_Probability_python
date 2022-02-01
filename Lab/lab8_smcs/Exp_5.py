import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import ztest as ztest

path = "C:\\Users\\Admin\\Downloads\\school.csv"
height = pd.read_csv(path)
print(height)

boys1 = height['Boys1'].tolist()
girls2 = height['Girls2'].tolist()

print(boys1)
print(girls2)

height_mean_boys = np.mean(height.Boys1)
print(height_mean_boys)

height_mean_girl1 = np.mean(height.Girls2)
print(height_mean_girl1)


zscore ,pval=ztest(boys1, girls2, value=0)
print(float(pval))
if pval<0.05:
 print("reject null hypothesis")
else:
 print("accept null hypothesis")

