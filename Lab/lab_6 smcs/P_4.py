import math 

def neg_geo_pdf(x, p, r):
    f = math.factorial
    a = f(x-1) / (f(r-1) * f(x-r))
    temp = math.pow(1-p , x -r )  * math.pow(p,r)
    result = a * temp
    print(result)


neg_geo_pdf(10, 0.2, 3)