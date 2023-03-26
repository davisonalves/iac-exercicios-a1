# 36 Uma pessoa só pode votar em eleições brasileiras se ela for maior que 16 anos
# e for cidadã brasileira. Desenvolva um método que leia uma lista previamente carregada
# com o nome de 10 pessoas. Em seguida, solicite a idade da pessoa, e sua nacionalidade,
# armazenando em listas paralelas. Por fim, verifique quantas pessoas estão aptas a votar
# ou não, de acordo com os dados armazenados.

nomes = ["Davison", "Levi", "Andre", "Anderson", "Luizao", "Fernando", "Wesley"]
idades = []
nacionalidades = []
aptos = 0

for nome in nomes:
    idade = int(input(f"Digite a idade de {nome}: "))
    nacionalidade = input(f"Informe a nacionalidade de {nome}: ")
    idades.append(idade)
    nacionalidades.append(nacionalidade)

    if idade > 16 and nacionalidade.lower() == 'brasil':
        aptos += 1
        print(f'{nome} pode votar!')
    else:
        print(f'{nome} não pode votar.')

print(f'Total de pessoas aptas a votar: {aptos}')