import math 

#PDF from exponialtial Distribution
def exp_dis_pdf(x , y):
    a = -(y * x)
    b = math.exp(a)
    result_pdf = y * b 
    print(result_pdf)
    
    
#CDF from exponialtial Distribution
    result_cdf  = 1 - b 
    print(result_cdf)

exp_dis_pdf(5 , 0.25)






