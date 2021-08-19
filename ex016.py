# crie um programa que leia um número real qualquer pelo teclado e mostre na tela
#  sua porção inteira.  ex:digite 6.127   >>>>o número 6.127 tem a parte inteira 6.
import math
num =float(input('digite um número: '))
print('o valor digite o foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
