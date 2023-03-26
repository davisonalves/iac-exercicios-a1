# 32 Crie uma lista com os nomes de uma turma de 20 alunos. Em seguida, elabore
# um método que solicite a idade de cada um, e armazene em uma lista paralela. Por fim,
# calcule a idade média da turma.

alunos = ["Davison", "Levi", "Andre", "Anderson", "Luizao", "Fernando", "Wesley"]
idades = []

for aluno in alunos:
    idade = int(input(f"Informe a idade do(a) aluno(a) {aluno}? "))
    idades.append(idade)
idade_media = sum(idades) / len(idades)
print(f"A idade média da turma é {idade_media:.2f} anos.")
