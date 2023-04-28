#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 09:58:51 2023

Exercise 1: 
    
    Write a while loop that only accepts integer numbers.
    Use the input function, and if the user inputs 
    anything other than a number,
    have the user try again.

@author: yin
"""

while True:
    try:
        user_num = int(input('Please enter a number: '))
        print(f'{user_num} is a valid integer')
        break
    except Exception as err:
        print(f'Error generated: {err} of type {type(err)}')
        

# while True:
#     try:
#         user_num = int(input('Please enter a number: '))
#         print(f'{user_num} is a valid integer')
#         break
#     except ValueError as err:
#         print(f'Error generated: {err} of type {type(err)}')