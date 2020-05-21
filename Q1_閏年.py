# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:13:22 2020

@author: ponywu001
"""

"""
進階程式設計 HW-1
"""

for i in range(eval(input())):
    year = eval(input())
    
    if year % 4 == 0 and year % 100 != 0:
        print(1)
    elif year % 400 == 0:
        print(1)
    else:
        print(0)