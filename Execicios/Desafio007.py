#Faça um programa que leia o preço de um produto, e mostre seu novo
#preço, com 5% de desconto.

preco = float(input('Digite o preço do produto R$: '))
print(f'Com desconto de 5% o produto saira por apenas R$' + '{:.2f}'.format(preco - ((preco * 5) / 100)))