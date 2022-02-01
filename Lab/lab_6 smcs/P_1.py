import math

#PDF from Bionomial Distribution
def binomial_pdf(x,p,n):
    a= math.factorial(n)
    b= math.factorial(x)
    c =math.factorial(n-x)
    
    temp= a/ (b*c)
    result = temp * math.pow(0.3,2) * math.pow(0.7 , 10)
    print(result)
    
binomial_pdf(2,0.3,12)

#CDF from Bionomial Distribution
    
p , x , n  = 0.3 , 2 , 12

for i in range(x):
    u = math.factorial(n)
    v = math.factorial(i)
    w =math.factorial(n-i)
    temp2=  u / (v *w)
    result_cdf = temp2 * math.pow(0.3,i) * math.pow(0.7 , n -i)
    print(result_cdf)