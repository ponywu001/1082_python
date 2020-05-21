# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 21:14:57 2020

@author: ponywu001
"""

"""
進階程式設計 HW-6
"""

  
for i in range(eval(input())):
    money = eval(input())

    card = money
    bread = money

    while card >= 3:
        bread += card//3
        card = card % 3 + card // 3
    
    print(bread)