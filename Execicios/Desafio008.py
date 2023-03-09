#Faça um programa que leia o salário de um funcionário, e mostre seu novo
#salário, com 15% de aumento.

salario = float(input('Digite o seu salário atual: '))
print(f'Com seu novo aumento de 15% o seu novo salário será de R$' + '{:.2f}'.format(salario + ((salario * 15) / 100)))