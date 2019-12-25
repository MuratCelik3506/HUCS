# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:27:02 2019

@author: murat
. Writeafunctionthatdetermines ifthegiveninputstringisa
Palindrome ornot.

"""

word = input()
x = word[::-1]
print(x)
if x == word:
    print(True) 
else:
    print('Yeniden dene')