#Faça um algoritimo que leia o preço do produto e mostre seu novo preço com 5% de desconto.
preço = float(input('digite o preço'))
novo = preço - (preço * 5 / 100)
print('o preço do produto de valor {} com desconto de 5% é {}' .format(preço, novo))
