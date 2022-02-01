#problem 1

from statsmodels.stats.weightstats import ztest as ztest


data = [1.8, 1.6, 2.6, 2.7, 2.8, 2.2, 1.2, 3.2, 1.5, 1.6, 1.6, 2.0, 3.0, 1.5, 1.4, 2.2, 1.9, 1.8, 1.9, 1.8, 1.7,
1.6, 1.2, 1.9, 2.0, 2.0, 1.8, 1.9, 1.8, 1.7, 1.6, 1.2, 1.9, 2.0, 2.0, 1.8, 1.9, 1.8, 1.7, 1.6, 1.2, 1.9,
2.0, 2.0]


zscore ,pval=ztest(data, value=2.0)
print(float(pval))
if pval<0.05:
 print("reject null hypothesis")
else:
 print("accept null hypothesis")
 
 
#Since this p-value is not less than .05, 
#we do not have sufficient evidence to reject the null hypothesis.


#problem 2

from statsmodels.stats.weightstats import ztest as ztest


variety_A = [23, 24, 25, 23, 22, 24, 23,23, 26, 21, 22, 23, 24, 20, 25, 23, 22, 23, 24, 25, 23, 22, 24, 23,23,
26, 21, 22, 23, 24, 20, 25, 23, 22, 23, 24, 25, 23, 22, 24, 23,23, 26, 21, 22, 23, 24, 20, 25, 23,
22]

variety_B = [20, 19, 18, 18, 22, 20, 19, 18, 18, 22, 21, 22, 21, 18, 23, 23, 22, 20, 21, 20, 21, 19, 19, 21, 22,
21, 18, 23, 23, 22, 20, 21, 20, 21, 19, 19, 20, 19, 18, 18, 22, 21, 22, 21, 18, 23, 23, 22, 20, 21,
20]


zscore ,pval=ztest(variety_A, variety_B, value=0)
print(float(pval))
if pval<0.05:
 print("reject null hypothesis")
else:
 print("accept null hypothesis")

#Since this p-value is less than .05, 
#we have sufficient evidence to reject the null hypothesis.