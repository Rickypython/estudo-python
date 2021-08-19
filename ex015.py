# Escreva um progrma que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar,sabendo que o carro custa R$60,00 por dia e R$0,15  por Km rodado.
dias = int(input('quantos dias alugados? '))
km = float (input('quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('o total a pagar é de {:.2f}'.format(pago))
