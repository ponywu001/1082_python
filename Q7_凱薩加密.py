# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:15:05 2020

@author: ponywu001
"""

"""
進階程式設計 HW-7
"""

s = [eval(x) for x in input().split(" ")]
for i in range(s[1]):
    a = list(input())
    
    for j in a:
        c = (ord(j) - s[1] - 97)
        if c < 0:
            c += 26
        print(chr(c + 97),end='') 
    print()        