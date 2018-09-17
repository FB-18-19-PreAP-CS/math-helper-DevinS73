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
        return "Divide by zero error"
    if b**2-4*a*c<0:
        answer1=(sqrt(abs(b**2-4*a*c))-b)/(2*a)
        answer2=(sqrt(abs(b**2-4*a*c))*-1-b)/(2*a)
        return str(round(answer1,4))+'*i',str(round(answer2,4))+'*i'
    if b**2-4*a*c==0:
        answer1=(-b)/(2*a)
        return round(answer1,4)
    if b**2-4*a*c>0:
        answer1=(sqrt(b**2-4*a*c)-b)/(2*a)
        answer2=(sqrt(b**2-4*a*c)*-1-b)/(2*a)
        answer1=round(answer1,4)
        return round(answer1,4), round(answer2,4)
print(quadratic(-6,-7,-3))