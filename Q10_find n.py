# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:45:37 2020

@author: ponywu001
"""

import math

for i in range(eval(input())):
    num = eval(input())
    
    if num ** (1/2) % 1 == 0:
        print(math.ceil(num ** (1/2)) + 1, end = " ")
    else:
        print(math.ceil(num ** (1/2)), end = " ")
        
    if num ** (1/3) % 1 == 0:
        print(math.floor(num ** (1/3)) - 1)
    else:
        print(math.floor(num ** (1/3)))