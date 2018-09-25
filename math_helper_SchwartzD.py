from math import sqrt
from decimal import Decimal, getcontext
import doctest
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
        two values and the number of the list at which they appear.
        Values can vary from true values by .00001
        
    >>> geometric_first(12,34e100,56**5600,98e97)
    Traceback (most recent call last):
        ...
    OverflowError: One or more of the variables is too large
    
    >>> geometric_first(4,16,5,32)
    Decimal('2')
    
    >>> geometric_first(1,6,100000,243542)
    Decimal('6')
    
    >>> geometric_first(6,1/112,10,1/1792)
    Decimal('0.28572')
    
    >>> geometric_first(6.2,121,10.5,42)
    Traceback (most recent call last):
        ...
    ValueError: Both terms must be whole numbers
    
    >>> geometric_first(-2,7,-33,232)
    Traceback (most recent call last):
        ...
    ValueError: Neither term can be less than or equal to 0
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
        return Decimal(value1)
    if term2==2:
        return Decimal(value2)
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
    while True:
        print('')
        print('Quadratic equation: ax^2+bx+c')
        a=input('Enter the value of a: ')
        b=input('Enter the value of b: ')
        c=input('Enter the value of c: ')
        print('')
        try:
            a=float(a)
            b=float(b)
            c=float(c)
        except Exception as e:
            print('Error: One or more of the inputs was invalid')
        if type(a)==float and type(b)==float and type(c)==float:
            try:
                if type(quadratic(a,b,c))==float:
                    print(f"The answer for the provided quadratic values is {quadratic(a,b,c)}.")
                    return
                if len(quadratic(a,b,c))==2:
                    print(f"The answers for the provided quadratic values are {quadratic(a,b,c)[0]} and {quadratic(a,b,c)[1]}.")
                    return
            except Exception as e:
                print(f"Error: {e}")
def use_distance():
    while True:
        print('')
        x=input('Enter the x value of the first point: ')
        y=input('Enter the y value of the first point: ')
        x1=input('Enter the x value of the second point: ')
        y1=input('Enter the y value of the second point: ')
        print('')
        try:
            x=float(x)
            y=float(y)
            x1=float(x1)
            y1=float(y1)
        except Exception as e:
            print('Error: One or more of the inputs was invalid')
        if type(x)==float and type(y)==float and type(x1)==float and type(y1)==float:
            try:
                print(f"The distance between the points ({x},{y}) and ({x1},{y1}) is {distance(x,y,x1,y1)}.")
            except Exception as e:
                print(f"Error: {e}")
def use_comp_interest():
    initial=input('Enter the initial principal (amount of money): ')
    percent=input('Enter the percent of interest: ')
    compounded=input('Enter the number of times the amount is compounded annually: ')
    years=input('Enter the amount of years forward you would like to calculate: ')
    print('')
    try:
        initial=float(initial)
        percent=float(percent)
        compounded=float(compounded)
        years=float(years)
    except Exception as e:
        print('Error: One or more of the inputs was invalid')
    if type(initial)==float and type(percent)==float and type(compounded)==float and type(years)==float:
        try:
            print(f"After {years} year(s), with an interest rate of {percent}% compounded \n {compounded} times a year, ${initial} will become ${comp_interest(initial, percent, compounded,years)}.")
            return
        except Exception as e:
            print(f"Error: {e}")
def use_geometric_nth_term():
    first=input('Enter the first term of the sequence: ')
    common_ratio=input('Enter the common ratio between terms in the sequence: ')
    given=input('Enter the number of the term you would like to find: ')
    print('')
    try:
        first=float(first)
        common_ratio=float(common_ratio)
        given=float(given)
    except Exception as e:
        print('Error: One or more of the inputs was invalid')
    if type(first)==float and type(common_ratio)==float and type(given)==float:
        try:
            print(f"Term number {given} of a geometric sequence with the first term {first} and the \n common ratio {common_ratio} is {geometric_nth_term(given,first,common_ratio)}.")
        except Exception as e:
            print(f"Error: {e}")
def use_geometric_first():
    term1=input('Enter the term number of the first known term: ')
    value1=input('Enter the value of the first known term: ')
    term2=input('Enter the term number of the second known term: ')
    value2=input('Enter the value of the second known term: ')
    print('')
    try:
        term1=float(term1)
        value1=float(value1)
        term2=float(term2)
        value2=float(value2)
    except Exception as e:
        print('Error: One or more of the inputs was invalid')
    if type(first)==float and type(common_ratio)==float and type(given)==float:
        try:
            print(f"The first term of a geometric sequence with a value of {value1} at term {term1} and a value of {value2} at term {term2} is {geometric_first(term1,value1,term2,value2)}.")
        except Exception as e:
            print(f"Error: {e}")
def interface():
    while True:
        print(' ')
        print('Welcome to Math Helper v0.8')
        print('Input the number of the function you would like to use.')
        print('1. Find the value of a quadratic equation')
        print('2. Find the distance between two points')
        print('3. Use compound interest')
        print('4. Find the nth term of a geometric sequence')
        print('5. Find the first term of a geometric sequence')
        print('X. Cancel')
        selection=input('> ')
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
        elif selection=='x' or selection=='X':
            break
        else:
            print('You have entered an invalid input, please try again.')
if __name__=='__main__':
    doctest.testmod()
    interface()