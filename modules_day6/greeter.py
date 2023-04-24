#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:10:48 2023

Greeter functions with arbitrary number of arguments

@author: yin
"""

# arbitrary number of names and print out greeting messages


def greeter_names(*names, msg = 'Welcome to week 2!'):
    """
    Function takes in as many names as given and optional message.
    Prints out greetings per name

    Parameters
    ----------
    *names : str
    msg : str, optional
         Message to print. The default is 'Welcome to week 2!'.

    Returns
    -------
    None.
    """
    for name in names:
        print(name, msg)
        

def greeter_more(*names, **messages):
    """
    Function takes in arbitrary number of names and messages.
    Prints out each message per name
    
    :param *names: str, the names
    :param **messages: str, the messages as keyword arguments
        
    :returns None:
    """
    for name in names:
        for msgname, msg in messages.items():
            print(f'{msgname}:\t{name} {msg}')
            
if __name__ == "__main__":
    
    greeter_names('Harry', 'Ron')
    greeter_more('Hermione', msg = 'She is a witch.')

    

