# Faça um programa que leia a largura e a altura de uma parede em metros,calcule a sua área e a quantidade de
# tinta necessária para pinta=la,sabendo que cada litro de tinta,pinta uma área de 2m2
#2.5  1.75  2.1875
L = float(input('qual a largura da parede?'))
A = float(input('qual a altura da parede?'))
Ar = A*L
print('a medida da área da sua parede é {}, e vc vai precisar de {} litros para pintar essa parede' .format(Ar, Ar/2))
