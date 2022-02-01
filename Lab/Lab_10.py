print('Problem 1')


from scipy.stats import chi2_contingency
table=[[200,150,50],[250,300,50]]
print(table)
stat,p,dof,expected=chi2_contingency(table)
print('P value:', p)
if p > 0.05:
  print('Opinion poll result Distribution are same \n')
else:
  print('Opinion poll result Distribution are different \n')


print('Problem 2')
table=[[13,11,7,13],[15,18,11,5]]
print(table)
stat,p,dof,expected=chi2_contingency(table)
print('P value:', p)
if p > 0.05:
  print('Here gender claim in which Distribution are same \n')
else:
  print('Here gender claim in which Distribution are different \n')

print('Problem 3')
table=[[60,120,100],[90,200,350]]
print(table)
stat,p,dof,expected=chi2_contingency(table)
print('P value:', p)
if p > 0.05:
  print('Here book preference based on gender in which Distribution are same \n')
else:
  print('''Here book preference based on gender in which 
Distribution are same Distribution are different''')


