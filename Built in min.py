# calc_max_Ramon Torres AGO 21 2022
# original source Fig. 2.2: fig02_02.py 
"""Find the minumum of four values."""

number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
number3 = int(input('Enter third integer: '))
number4 = int(input('Enter third integer: '))

maximum = number1  

if number2 < maximum:
    minumum = number2

if number3 < minumum:
    minumum = number3

if number4 < minumum:
    minumum = number4

print('Minimum value is', minumum)