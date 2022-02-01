import math

#PDF from poission Distribution
def poisson_pdf(x,y):
    a= math.factorial(x)
    temp = math.exp(-y) * math.pow(y,x)
    result = temp / a
    print(result)
    
poisson_pdf(2,5)    


#CDF from poission Distribution
x ,y = 2 ,5 
for i in range(x):
    temp1 = math.factorial(i)
    temp2 = math.exp(-y) * math.pow(y,i)
    result_cdf  = temp2 / temp1
    print(result_cdf)