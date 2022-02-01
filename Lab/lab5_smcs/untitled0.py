import math
 
#PDF from Normal Distribution
def normal_PDF(x, mean, std_dev):
    probability = 1.0 / math.sqrt(2 * 3.141592*(std_dev)**2)  
    probability *= math.exp(-0.5 * ((x - mean)/std_dev)**2)  
 
 
    print(probability)
 
normal_PDF(39, 37, 2)


#CDF from Normal Distribution


def normal_cdf(x):
    "cdf for standard normal"
    q = math.erf(x / math.sqrt(2.0))
    result = (1.0 + q) / 2.0
    print(result)

normal_cdf(1.96)
