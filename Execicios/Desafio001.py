# Crie um programa que leia um número e mostre o seu dobro, seu triplo e sua
# raiz quadrada.

numero = int(input('Digite um número para saber seu dobro, triplo e sua raiz quadrada: '))
print(f'O dobro de {numero} é igual a: {numero * 2} \nO Triplo de {numero} é igual a: {numero * 3} \nA raiz quadrade de {numero} é igual a :' + '{:.2f}'.format(numero ** 0.5))

