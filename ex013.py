#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.j
S = float(input('digite o salário'))
ns = S+ (S * 15/100)
print('o valor do seu salário era {} e com 15% de aumento passou para{}' .format(S, ns))