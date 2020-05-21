# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:14:43 2020

@author: ponywu001
"""

"""
進階程式設計 HW-4
"""

for i in range(eval(input())):
    num = eval(input())
    sum = 0
    
    for j in range(num, 0, -1):
        sum += 1/j  
        
    print(sum)