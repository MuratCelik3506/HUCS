# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 23:59:20 2019

@author: murat
"""

a = 1
b = 1
x = 0

while b< 4000000:
    c = a + b
    a = b
    b = c
    if b % 2 == 0:
       x = b + x
print(x)
       
    