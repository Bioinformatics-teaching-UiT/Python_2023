#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:48:25 2023

Lambda functions

@author: yin
"""

def square(x):
    return x**2

square2 = lambda x : x**2

print(square2(2))

add = lambda x, y : x + y
subtract = lambda x, y : x - y
multiply = lambda x, y : x * y

print(multiply(2,3))
print(subtract(2,3))
print(add(2,3))


