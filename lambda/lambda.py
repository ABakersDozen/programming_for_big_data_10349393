###### exercise 1
# def fahrenheit(t):
    # return ((float(9)/5)*t + 32)
# def celsius(t):
    # return (float(5)/9)*(t - 32)
# temp = (36.5, 37, 37.5, 39)

# F = map(fahrenheit, temp)
# print F
# C = map(celsius, F)
# print C

###### exercise 2
# a = [1,2,3,4]
# b = [17,12,11,10]
# c = [-1, -4, 5, 9]
# print map(lambda x,y:x+y, a,b)
# print map(lambda x,y,z:x+y+z, a,b,c)
# print map(lambda x,y,z:x+y-z, a,b,c)

####### exercise 3
# fib = [0,1,1,2,3,5,8,13,21,34,55]
# result = filter(lambda x: x % 2, fib)
# print result

# result = filter(lambda x: x % 2 == 0, fib)
# print result

####### exercise 4
##print reduce(lambda x, y: x+y, range(1, 101))
# max function
# f = lambda a,b: a if (a>b) else b
# print reduce(f, range(1,101))
# # min function
# f = lambda a,b: a if (a<b) else b
# print reduce(f, range(1,101))

####### exercise 5
# def sum(values):
    # return reduce(lambda x,y: x+y, values)
# def max(values):
    # return reduce(lambda a,b: a if (a>b) else b, values)
# def min(values):
    # return reduce(lambda a,b: a if (a<b) else b, values)
# def add(first, second):
    # return map(lambda x, y: x+y, first, second)
# def is_even(values):
    # return filter(lambda x: x%2==0,values)    
# def greater_than_mean(values,mean):
    # return filter(lambda x: x>mean, values)
# def to_fahrenheit(values):
    # return [((float(9)/5)*x+32) for x in values]
# def divide(first,second):
    # return map(lambda x, y: x/float(y) if y!=() else 'NaN',first,second)

    
# values = [47,11,42,13]
# print sum(values)
# print max(values)
# print min(values)
# print add(values, [37,21,22,33])
# print is_even(values)
# print greater_than_mean(values,28)
# print to_fahrenheit(values)

####### exercise 6
#print [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]

####### exercise 7
# def city_generator():
    # yield("Konstanz")
    # yield("Zurich")
    # yield("Schaffhausen")
    # yield("Stuttgart")
# x = city_generator()
# print x.next()
# print x.next()
# print x.next()
# print x.next()
# print x.next() # this one will give an error

####### exercise 8
# def fibonacci(n):
    # """Fibonacci numbers generator, first n"""
    # a = 0
    # b = 1
    # counter = 0
    # while True:
        # if (counter > n): return
        # #print 'hi',
        # yield a
        # a = b
        # b = a + b
        # counter += 1
# f = fibonacci(10)
# for x in f:
    # print x, # comma keeps it on the same line for output with a space
    # #print 'ho',
# print  

# ####### exercise 9
# def pythagorean(n):
    # for x in range(1,n):
        # for y in range(x,n):
            # for z in range(y,n):
                # if x**2 + y**2 == z**2:
                    # yield (x,y,z)
# pyt = pythagorean(30)
# for triplet in pyt:
    # print triplet,
    # print sum(triplet)
    
 # ####### exercise 10   
# a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
# def flatten(values):
    # return (lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x])(values)
# print flatten(a)

# ####### exercise 11
'''Binomial theorem'''
# import math
# import operator
# def binomial_coeff(first,second):
    # return map(lambda m,n: reduce(operator.mul, xrange(m, n+1), 1),first,second)
    
# y = [1,2,3,4]
# x = [17,12,11,10]
# print binomial_coeff(y+1, x) / binomial_coeff(1, x-y)

# ####### exercise 12
# ''' compute combinatorials (nCr)'''
# from fractions import Fraction

# mul=lambda x,y:x*y

# def nCk(n,k): 
  # return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )
  
# for n in range(17):
    # print ' '.join('%5d'%nCk(n,k) for k in range(n+1)).center(100)

n = [17,12,11,10]    
k = [1,2,3,4]
# f=lambda x:+(x<2)or x*f(x-1)
# print f(n)/(f(k)*f(n-k))

def binomial_coeff(first,second):
    recurs = lambda x:+(x<2)or x*recurs(x-1)
    return list(map(recurs(n)/(recurs(k)*recurs(n-k)),first,second))
    
print binomial_coeff(n,k)
