import math
 
#PDF from Normal Distribution
def normal_PDF(x, mean, std_dev):
    probability = 1.0 / math.sqrt(2 * 3.14*(std_dev)**2)  
    probability *= math.exp(-0.5 * ((x - mean)/std_dev)**2)  
 
 
    print(probability)
 
normal_PDF(7, 10, 2.23)


#CDF from Normal Distribution


def normal_cdf(x):
    "cdf for standard normal"
    q = math.erf(x / math.sqrt(2.0))
    result = (1.0 + q) / 2.0
    print(result)

normal_cdf(7)
