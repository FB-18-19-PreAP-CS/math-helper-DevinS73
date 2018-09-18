from math import sqrt
from math import floor
'''
formula examples go
here
'''
def quadratic(a,b,c):
    '''returns answer when given a, b, and c
       from formula ax^2+bx+c
       
    >>> quadratic(9,9,9)
    '''
    if a==0:
        return "Error: Cannot divide by zero"
    if b**2-4*a*c<0:
        return "Error: Cannot take the square root of a negative number"
    if b**2-4*a*c==0:
        answer1=(-b)/(2*a)
        return round(answer1,4)
    if b**2-4*a*c>0:
        answer1=(sqrt(b**2-4*a*c)-b)/(2*a)
        answer2=(sqrt(b**2-4*a*c)*-1-b)/(2*a)
        answer1=round(answer1,4)
        return round(answer1,4), round(answer2,4)
def distance(x,y,x1,y1):
    x_squaredist=(x-x1)**2
    y_squaredist=(y-y1)**2
    dist=sqrt(x_squaredist+y_squaredist)
    return dist
def comp_interest(initial_amount,percent_interest,comp_per_year,years):
    return
print(quadratic(-6,-7,-3))