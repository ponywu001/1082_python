# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:14:37 2020

@author: ponywu001
"""

"""
進階程式設計 HW-3
"""

for i in range(eval(input())):
    num = eval(input())
    a = []
    
    for j in range(1, num):
        if num % j == 0:
            a.append(j)
    
    if num == sum(a):
        print("True")
    else:
        print("False")