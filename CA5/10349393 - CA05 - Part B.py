# -*- coding: utf-8 -*-
"""
CA05 for Programming for Big Data
Student Number: 103494393
Student Name: Maitiú Baxter
"""
values = [47,11,42,13]
values2 = [37,21,22,33]
arbitrary = 15

#### 1
def sum(values):
    return reduce(lambda x,y: x+y, values)

print sum(values)

#### 2
def max(values):
    return reduce(lambda a,b: a if (a>b) else b, values)

print max(values)

#### 3
def min(values):
    return reduce(lambda a,b: a if (a<b) else b, values)

print min(values)

#### 4
def add(first, second):
    return map(lambda x, y: x+y, first, second)

print add(values, values2)

#### 5
def is_even(values):
    return filter(lambda x: x%2==0,values)    

print is_even(values)

#### 6
def greater_than_mean(values,mean):
    return filter(lambda x: x>mean, values)

print greater_than_mean(values,arbitrary)

#### 7
def to_fahrenheit(values):
    return [((float(9)/5)*x+32) for x in values]

print to_fahrenheit(values)

#### 8
def divide(first,second):
    return map(lambda x, y: x/float(y) if y!=() else 'NaN',first,second)

print divide(values,values2)    

#### 9
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a = 0
    b = 1
    counter = 0
    while True:
        if (counter > n): return
        yield a
        a = b
        b = a + b
        counter += 1
f = fibonacci(10)
for x in f:
    print x, # comma keeps it on the same line for output with a space
print  

#### 10
def pythagorean(n):
    for x in range(1,n):
        for y in range(x,n):
            for z in range(y,n):
                if x**2 + y**2 == z**2:
                    yield (x,y,z)
pyt = pythagorean(30)
for triplet in pyt:
    print triplet,
    print sum(triplet)
    
#### 11 
''' Flatten Lists '''   
a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
def flatten(values):
    return (lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x])(values)
print flatten(a)

#### 12
'''Binomial theorem'''

''' compute combinatorials (nCr)'''
from fractions import Fraction

mul=lambda x,y:x*y

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

# run this in DOS, interesting layout  
for n in range(17):
   print ' '.join('%5d'%nCk(n,k) for k in range(n+1)).center(100)
