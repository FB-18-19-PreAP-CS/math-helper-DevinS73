from math import sqrt
from decimal import Decimal, getcontext
#nthroot from https://rosettacode.org/wiki/Nth_root#Python
def nthroot (n, A, precision):
    getcontext().prec = precision
 
    n = Decimal(n)
    x_0 = A / n #step 1: make a while guess.
    x_1 = 1     #need it to exist before step 2
    while True:
        #step 2:
        x_0, x_1 = x_1, (1 / n)*((n - 1)*x_0 + (A / (x_0 ** (n - 1))))
        if x_0 == x_1:
            return x_1
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
def comp_interest(initial,percent,compounded,years):
    if years<0:
        return "Error: Cannot have negative years"
    if compounded<=0:
        return "Error: Cannot compound 0 or less times annually"
    amount=initial*(1+(percent/100)/compounded)**(compounded*years)
    return round(amount,2)
def geometric_nth_term(given,first,common_ratio):
    nth_term=first*common_ratio**(given-1)
    return nth_term
def geometric_first(term1,value1,term2,value2):
    if term1>term2:
        r=nthroot(term1-term2,value1/value2,20)
        answer=value2
    if term2>term1:
        r=nthroot(term2-term1,value2/value1,20)
        answer=value1