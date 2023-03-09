#Crie um programa que leia o quanto uma pessoa tem na carteira e mostre
#quantos dólares ela pode comprar.

valor = float(input('Digite quanto tem em R$ : '))
print(f'Esse valor é equivalente à US$'+ '{:.2f}'.format(valor / 5))