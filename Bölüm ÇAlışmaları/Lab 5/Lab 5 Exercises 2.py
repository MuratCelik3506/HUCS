# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:06:53 2019

@author: murat


Write a Boolean function that checks if a string contains ‘@’ sign and at least one ‘.’ dot
 ( disregard the order for the sake of simplicity) .Use that function to check if a user input 
 is a valid e-mail or not.
""" 
mail = input('bisiler yaz')
x = mail.count('.')
y = mail.count('@')
if x>=1 and y >= 1:
   print(True)
else:
   print(False)
    
    
