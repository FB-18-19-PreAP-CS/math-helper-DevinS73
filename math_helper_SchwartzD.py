from math import sqrt
from decimal import Decimal, getcontext
import doctest
doctest.testmod()
#nthroot from https://rosettacode.org/wiki/Nth_root#Python (used in geometric_first)
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
    ''' returns the zeroes of an equation using
        the quadratic formula
       
    >>> quadratic(9,9,9)
    Traceback (most recent call last):
        ...
    ValueError: Cannot take the square root of a negative number
    
    >>> quadratic(0,1,2)
    Traceback (most recent call last):
        ...
    ValueError: a cannot be zero
    
    >>> quadratic(1e1000,2222,8**15)
    Traceback (most recent call last):
        ...
    OverflowError: One or more of the variables is too large
    
    >>> quadratic(4,8,4)
    -1.0
    
    >>> quadratic(3,6,-5)
    (0.633, -2.633)
    '''
    if a+1==a or b+1==b or c+1==c:
        raise OverflowError('One or more of the variables is too large')
    if a==0:
        raise ValueError('a cannot be zero')
    if b**2-4*a*c<0:
        raise ValueError("Cannot take the square root of a negative number")
    if b**2-4*a*c==0:
        answer1=(-b)/(2*a)
        return round(answer1,4)
    if b**2-4*a*c>0:
        answer1=(sqrt(b**2-4*a*c)-b)/(2*a)
        answer2=(sqrt(b**2-4*a*c)*-1-b)/(2*a)
        answer1=round(answer1,4)
        return round(answer1,4), round(answer2,4)
def distance(x,y,x1,y1):
    ''' returns the distance between points (x,y)
        and (x1,y1)
       
    >>> distance(9,9,9,9)
    0.0
    
    >>> distance(9,9,9,20)
    11.0
    
    >>> distance(1e1000,2222,123456^789,6)
    Traceback (most recent call last):
        ...
    OverflowError: One or more of the variables is too large
    
    >>> distance(80,4,8,4)
    72.0
    
    >>> distance(0,0,10,10)
    14.1421
    '''
    if x+1==x or x1+1==x1 or y+1==y or y1+1==y1:
        raise OverflowError('One or more of the variables is too large')
    x_squaredist=(x-x1)**2
    y_squaredist=(y-y1)**2
    dist=sqrt(x_squaredist+y_squaredist)
    return round(dist,4)
def comp_interest(initial,percent,compounded,years):
    ''' returns the compound interest after a given number of
        years
       
    >>> comp_interest(10000,0,9,9)
    10000.0
    
    >>> comp_interest(10000,100,10,0)
    10000.0
    
    >>> comp_interest(10000,5,2,5)
    12800.85
    
    >>> comp_interest(1,2222^222,1e100,7)
    Traceback (most recent call last):
        ...
    OverflowError: One or more of the variables is too large
    
    >>> comp_interest(12,34,56,-2)
    Traceback (most recent call last):
        ...
    ValueError: Years cannot be negative
    
    >>> comp_interest(123,345,-567,890)
    Traceback (most recent call last):
        ...
    ValueError: Number of times compounded annually cannot be less than zero
    '''
    if initial+1==initial or percent+1==percent or compounded+1==compounded or years+1==years:
        raise OverflowError('One or more of the variables is too large')
    if years<0:
        raise ValueError('Years cannot be negative')
    if compounded<=0:
        raise ValueError("Number of times compounded annually cannot be less than zero")
    amount=initial*(1+(percent/100)/compounded)**(compounded*years)
    return round(amount,2)
def geometric_nth_term(given,first,common_ratio):
    ''' returns the nth term of a geometric sequence given the 
        first term and common ratio
       
    >>> geometric_nth_term(12,34e100,56**5600)
    Traceback (most recent call last):
        ...
    OverflowError: One or more of the variables is too large
    
    >>> geometric_nth_term(10.11211221,2,2)
    Traceback (most recent call last):
        ...
    ValueError: Term given to find must be a whole number
    
    >>> geometric_nth_term(-13,8,5)
    Traceback (most recent call last):
        ...
    ValueError: Term given to find cannot be negative
    
    >>> geometric_nth_term(11,1000,8/13)
    7.7887
    
    >>> geometric_nth_term(1,123456789,787878787)
    123456789
    '''
    if given+1==given or first+1==first or common_ratio+1==common_ratio:
        raise OverflowError('One or more of the variables is too large')
    if given<1:
        raise ValueError('Term given to find cannot be negative')
    if given-given//1!=0:
        raise ValueError('Term given to find must be a whole number')
    nth_term=first*common_ratio**(given-1)
    return round(nth_term,4)
def geometric_first(term1,value1,term2,value2):
    ''' returns the first term of a geometric sequence given 
        two values and the number of the list at which they appear
    >>> geometric_nth_term(12,34e100,56**5600,98e97)
    Traceback (most recent call last):
        ...
    OverflowError: One or more of the variables is too large

    '''
    if term1+1==term1 or value1+1==value1 or term2+1==term2 or value2+1==value2:
        raise OverflowError('One or more of the variables is too large')
    negative_ratio=False
    if value1<0 and value2>0:
        value1=abs(value1)
        negative_ratio=True
    if value2<0 and value1>0:
        value2=abs(value2)
        negative_ratio=True
    if value1<0 and value2<0:
        value1=abs(value1)
        value2=abs(value2)
    if term1<=0 or term2<=0:
        raise ValueError('Neither term can be less than or equal to 0')
    if term1-term1//1!=0 or term2-term2//1!=0:
        raise ValueError('Both terms must be whole numbers')
    if term1==1:
        return value1
    if term2==2:
        return value2
    if term1>term2:
        r=nthroot(term1-term2,value1/value2,5)
        answer=Decimal(value2)
        for i in range(term2,1,-1):
            answer/=r
    if term2>term1:
        r=nthroot(Decimal(term2-term1),Decimal(value2/value1),5)
        answer=Decimal(value1)
        for i in range(term1,1,-1):
            answer/=r
    if negative_ratio==False:
        return answer
    if negative_ratio==True:
        return -1*answer
def use_quadratic():
    print('quadratic equation: ax^2+bx+c')
    a=float(input('Enter the value of a: '))
    b=float(input('Enter the value of b: '))
    c=float(input('Enter the value of c: '))
def use_distance():
    x=float(input('Enter the x value of the first point: '))
    y=float(input('Enter the y value of the first point: '))
    x1=float(input('Enter the x value of the second point: '))
    xy=float(input('Enter the y value of the second point: '))
def use_comp_interest():
    initial=float(input('Enter the initial principal (amount of money): '))
    percent=float(input('Enter the percent of interest: '))
    compounded=float(input('Enter the number of times the amount is compounded annually: '))
    years=float(input('Enter the amount of years forward you would like to calculate: '))
def use_geometric_nth_term():
    first=float(input('Enter the first term of the sequence: '))
    common_ratio=float(input('Enter the common ratio between terms in the sequence: '))
    given=float(input('Enter the number of the term you would like to find: '))
def use_geometric_first():
    term1=float(input('Enter the number of the first known term: '))
    value1=float(input('Enter the value of the first known term: '))
    term2=float(input('Enter the number of the second known term: '))
    value2=float(input('Enter the value of the second known term: '))
def interface():
    print('Welcome to Math Helper v0.8')
    print('Input the number of the function you would like to use.')
    print('1. Find the value of a quadratic equation')
    print('2. Find the distance between two points')
    print('3. Use compound interest')
    print('4. Find the nth term of a geometric sequence')
    print('5. Find the first term of a geometric sequence')
    print('6. Cancel')
    while True:
        selection=input('>')
        if selection=='1':
            use_quadratic()
        elif selection=='2':
            use_distance()
        elif selection=='3':
            use_comp_interest()
        elif selection=='4':
            use_geometric_nth_term()
        elif selection=='5':
            use_geometric_first()
        elif selection=='6':
            break
        else:
            print('You have entered an invalid input, please try again')