# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:36:08 2019

@author: murat
Write a function perfect that determines if a number given as a
parameter is a perfect number or not. Use this function in a
program that determines and prints all the perfect numbers
between 1 and 1000.
"""

Sayi = int(input(" Bir sayi giriniz: "))
x = 0
for i in range(1, Sayi):
    if(Sayi % i == 0):
        x = x + i
if (x == Sayi):
    print(" %d is a Perfect Number" %Sayi)
else:
    print(" %d is not a Perfect Number" %Sayi)