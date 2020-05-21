# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:14:31 2020

@author: ponywu001
"""

"""
進階程式設計 HW-2
"""

a = []

for i in range(eval(input())):
    s = [x for x in input().split(" ")]
    p = int(s[1]) / 1000 + int(s[2]) - int(s[3])
    a.append((s[0], int(p)))

a.sort(key=(lambda x:x[1]))

for i in range(len(a)):
    print(a[i][0], a[i][1])
