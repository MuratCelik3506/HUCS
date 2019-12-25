# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:36:46 2019

@author: murat

2. Implementthe following integer functions:
• a)FunctioncelciusreturnstheCelsiusequivalentofaFahrenheit
temperature.
• b) Function fahrenheit returns the Fahrenheit equivalent of a Celsius
temperature.
"""

print('Bir fahr degeri giriniz')
fahr = int(input())
celc= (fahr-32) * 5/ 9
print(celc)