# 34 Desenvolva um método que imprima a soma dos números de 1 até 1000.

def soma_ate_mil():
    soma = 0
    for contador in range(1, 1001):
        soma += contador
        print(f'A soma é {soma}')
    print(f"A soma dos números de 1 a 1000 é:{soma}")
soma_ate_mil()
