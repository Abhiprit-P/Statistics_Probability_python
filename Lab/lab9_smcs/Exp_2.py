from scipy.stats import chisquare

f_exp =[173,150,311,519]
f_obs =[206,293,462,739]


stat,p= chisquare(f_obs, f_exp)
print('P value:', p)
if p > 0.05:
    print('Distribution are same')
else:
    print('Distribution are different')

print('''Since the p-value (1.01) is not less than 0.05, 
      we fail to reject the null hypothesis and to 
      believe that that the old percentagesno longer hold.''')
      