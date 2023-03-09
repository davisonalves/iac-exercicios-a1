#Escreva um programa que pergunte a quantidade de km percorridos por
#um carro alugado, e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
#pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

kmPercorrido = float(input('Digite quantos km foram percorridos: '))
diasAlugados = int(input('Digite dias passou com o carro: '))
preco = (60 * diasAlugados) + (0.15 * kmPercorrido)
print('Você deve pagar o valor de R$' + '{:.2f}'.format(preco))