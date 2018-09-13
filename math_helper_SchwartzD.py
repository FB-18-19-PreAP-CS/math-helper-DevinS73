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
    if a==0:
        return "Divide by zero error"
    if b**2-4*a*c<0:
        answer1=(sqrt(abs(b**2-4*a*c))-b)/(2*a)
        answer2=(sqrt(abs(b**2-4*a*c))*-1-b)/(2*a)
        return str(answer1)+'*i'
    if b**2-4*a*c>=0:
        answer1=(sqrt(b**2-4*a*c)-b)/(2*a)
        answer2=(sqrt(b**2-4*a*c)*-1-b)/(2*a)
    return answer1, answer2
print(quadratic(6,-7,-3))