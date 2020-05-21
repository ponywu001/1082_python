# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:14:50 2020

@author: ponywu001
"""

"""
進階程式設計 HW-5
"""

for i in range(eval(input())):
    num = eval(input())
    sum = 0
    a = 1
    
    for j in range(1, num+1):
        a *= j
        sum += a
        
    print(sum)