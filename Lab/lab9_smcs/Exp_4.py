from scipy.stats import chisquare

f_exp =[40,40,40,40,40,40]
f_obs =[34,44,30,46,51,35]


stat,p= chisquare(f_obs, f_exp)
print('P value:', p)
if p > 0.05:
    print('Distribution are same')
else:
    print('Distribution are different')

print('''Since the p-value (0.005) is not less than 0.05, 
     we fail to reject the null hypothesis, that the die is fair.''')

