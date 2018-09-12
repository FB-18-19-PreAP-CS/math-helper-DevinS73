from math import sqrt
'''
formula examples go
here
'''
def quadratic(a,b,c):
    '''
returns answer when given a, b, and c
from formula ax^2+bx+c
    '''
    if a!=0 and b**2-4*a*c>=0:
        answer1=(sqrt(b**2-4*a*c)-b)/2*a
        answer2=(sqrt(b**2-4*a*c)*-1-b)/2*a
    return answer1