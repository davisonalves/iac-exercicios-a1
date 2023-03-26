# 38 Desenvolva um método que some e exiba todos os números de 1 a 100,
# pulando os múltiplos de 3.

def soma():
    soma = 0

    for i in range(1, 100):
        if i % 3 != 0:
            soma += i
            print(f'Não multiplos de 3: {i} a soma é = {soma}')
soma()