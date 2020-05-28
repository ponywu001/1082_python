# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:15:05 2020

@author: ponywu001
"""

"""
進階程式設計 HW-7
"""

a, b = map(int, input().split(" ")
for i in range(b):
    s = list(input())
    
    for j in s:
        c = (ord(j) - b - 97)
        if c < 0:
            c += 26
        print(chr(c + 97),end='') 
    print()        
