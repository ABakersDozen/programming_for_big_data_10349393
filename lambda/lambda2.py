# -*- coding: utf-8 -*-
"""
Created on Wed May 10 18:33:06 2017

@author: macan
"""

def fahrenheit(t):
    return ((float(9)/5)*t + 32)
def celsius(t):
    return (float(5)/9)*(t - 32))
temp = (36.5, 37, 37.5, 39)

F = map(fahrenheit, temp)
print F
C = map(celsius, F)
print C