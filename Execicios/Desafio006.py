#Faça um programa que leia a largura e a altura de uma parede em metros,
#e calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
#litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite quanto a parede tem em largura: '))
altura = float(input('Digite quanto a parede tem em altura: '))
area = altura * largura
tinta = area / 2
print(f'Para pintar a parede será necessário utilizar {tinta} lt de tinta')