
#PDF from Uniform Distribution
def uniform_dis_pdf(a ,b ):    
         pdf = 1 / (b - a  )
         print(pdf)
   
        
uniform_dis_pdf(0 ,40 )    
    
#CDF from Uniform Distribution 

x = int(input('Enter the number for x :'))
y = int(input('Enter the number for y :'))
for i in range(x ,y):
    if i < x:
        print(0)
    elif i > y:
        print(1)
    else: 
        result = (i -x) / (y- x)
        print(result)