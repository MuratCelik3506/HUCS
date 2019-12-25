# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 17:56:10 2019

@author: murat

Write a program that asks for a number. N as a user input ,and calculates the sum of odd numbers,
 and the average of even numbers starting from 1 up to and including N.
"""

print('pozitif bir sayi giriniz')
sayi = int(input())
if sayi<=0 :
    print('Hatalı Sayi')
    pass
x = 0
y = 1
while sayi >= y:
   x = x + y
   y = y + 2

print(x)  
    




#####################################################3
z = 0
a = 2
i = 0
while sayi >= a :
      z = z + a
      a = a + 2
      i = i + 1
print(z/i)