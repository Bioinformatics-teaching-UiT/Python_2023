# -*- coding: utf-8 -*-
"""
Spyder Editor

Demo for exception handling with
try and except

"""

# division by zero problem

def run_calc(num):
    return num / 0

# catch zero division error

try:
    run_calc(6)
except ZeroDivisionError:
    print('You cannot divide by zero.')
    
# catch all errors / exceptions

try:
    run_calc(6)
except:
    print('Refresh your math skills.')
    
# show which error

try:
    run_calc(6)
except Exception as err:
    print(err) # prints out error statement
    print(type(err)) # prints out type of error
    
# catch the right type of error out of many possibilities
# aka multiple except statements

try:
    run_calc(nonexistent_var)
except ZeroDivisionError:
    print('Cannot divide by zero.')
except TypeError:
    print('Invalid type')
except Exception as err:
    print(f'Your code generated an error of type: {type(err)}')
    
    