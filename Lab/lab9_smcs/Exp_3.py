from scipy.stats import chisquare

f_exp =[220,220,220,220,220]
f_obs =[262,234,204,190,210]


stat,p= chisquare(f_obs, f_exp)
print('P value:', p)
if p > 0.05:
    print('Distribution are same')
else:
    print('Distribution are different')

print('''Since the p-value (0.005) is not less than 0.05, 
      we fail to reject the null hypothesis.and to believe 
      that customers do not prefer each of the 
      five stores equal''')


