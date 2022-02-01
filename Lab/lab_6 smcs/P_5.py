import math

#PDF from hyper_geo Distribution
def hyper_geo_pdf(N ,n , m , x):
    
    f = math.factorial
    x ,y =(N - m) , (n - x)
    
    a = f(m) / (f(x) * f(m - x))
    b = f(x) / (f(y) * f(x - y))
    c = f(N) / (f(n) * f(N - n))
    result_pdf = (a * b) / c
    print(result_pdf)


hyper_geo_pdf(20, 5 ,6 , 4)    

