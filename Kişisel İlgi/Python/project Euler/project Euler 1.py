# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:58:47 2019

@author: murat
"""

"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""


x= ((999-3)/3+1) * ((999+3)/2)
y= ((995-5)/5+1) * ((995+5)/2)
z= ((990-15)/15+1) * ((990+15)/2)
print(x+y-z)
