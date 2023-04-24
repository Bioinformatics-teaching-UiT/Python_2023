#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:28:24 2023

Demo on modules

@author: yin
"""

import greeter

# use our functions

greeter.greeter_names('Yin', 'Mobina', 'Laureen', msg = 'It is monday')


# import all functions in one go

from greeter import greeter_more, greeter_names

greeter_more('Bob', 'Sally', msg1 = 'It is sunny', msg2 = 'I prefer rain', msg3 = 'Bye')


# import functions as some other alias/name

import greeter as g

g.greeter_names('Yin')

print(dir(greeter))







