import math
#PDF from geometric Distribution
def geometric_pdf(x , p):
    q = 1-p
    
    result =  math.pow(q , x -1 ) * p
    print (result)

geometric_pdf(6,0.04)

#CDF from geometric Distribution
x , p =6 , 0.4
q = 1 - p
result_cdf = 1 - math.pow(q , x)
print(result_cdf)