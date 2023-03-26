# 31 Desenvolva um método que verifique se um número informado é:
# - Se é par ou ímpar
# - Se é multiplo de 2
# - Se é multiplo de 3
# - Se é multiplo de 5


def verificar_numero():

    numero = int(input('Digite o número a ser verificado: '))

    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

    if numero % 2 == 0:
        print("O número é múltiplo de 2.")
    else:
        print("O número não é múltiplo de 2.")

    if numero % 3 == 0:
        print("O número é múltiplo de 3.")
    else:
        print("O número não é múltiplo de 3.")

    if numero % 5 == 0:
        print("O número é múltiplo de 5.")
    else:
        print("O número não é múltiplo de 5.")


verificar_numero()
