from scipy.stats import chisquare
stat,p= chisquare(f_obs=[121,288,91], f_exp=[100,150,250])
print('P value:', p)
if p > 0.05:
    print('Distribution are same')
else:
    print('Distribution are different')
    

print('''Since the p-value (3.27) is not less than 0.05, 
      we fail to reject the null hypothesis. This means we do not have 
      sufficient evidence to say that that the population distribution 
      of ages has changed in the last 10 years''')