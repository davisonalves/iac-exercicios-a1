# 33 Utilizando uma lista com nomes de pessoas, previamente carregada, elabore
# um método solicite a idade de cada um, armazene na mesma ordem em outra lista, e
# exiba quantas pessoas possuem mais de 18 anos. Seu código deverá ler a idade de 10
# pessoas.

nomes = ["Davison", "Levi", "Andre", "Anderson", "Luizao", "Fernando", "Wesley"]
idades = []
for nome in nomes:
    idade = int(input(f"Digite a idade de {nome}: "))
    idades.append(idade)
mais_de_18 = 0
for idade in idades:
    if idade > 18:
        mais_de_18 += 1
print(f"Das {len(nomes)} pessoas, {mais_de_18} possuem mais de 18 anos.")
