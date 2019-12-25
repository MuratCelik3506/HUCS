# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:52:49 2019

@author: murat

Guessing game! Pick a number randomly. While user does not guess the number correctly give an instruction about the number and take another guess from user.
Instruction: If the guessed numberis lowerthan the picked number print
«increase yournumber»
else print
«decrease yournumber»
"""

import random
x = random.randint(0,10)
i=0
while i<10:
    sayi = int(input('Sayi gir'))

    i = i + 1
    if sayi == x :
        print(True)
        break
    else:
        if sayi < x:
            print('increase yournumber')
        else:
            print("decrease your number")
