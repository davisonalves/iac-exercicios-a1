#Faça um programa que leia um número inteiro e mostre na sua tela a sua
#tabuada.

numero = int(input('Digite um numero para visualizar sua tabuada: '))
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')