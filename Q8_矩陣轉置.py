# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:15:10 2020

@author: ponywu001
"""

"""
進階程式設計 HW-8
"""

for i in range(eval(input())):
    s = [eval(x) for x in input().split(" ")]
    a = [[0]*s[0] for i in range(s[1])]
    for j in range(s[0]):
        l = input().split()
        for z in range(s[1]):
            a[z][j] = l[z]
    for i in a:
        print(*i)