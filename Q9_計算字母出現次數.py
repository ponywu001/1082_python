# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:15:16 2020

@author: ponywu001
"""

"""
進階程式設計 HW-9
"""

s = [x for x in input().split(" ")]

for i in range(97, 123):
    print(chr(i), s.count(chr(i)))