# Crie uma lista com os nomes de uma turma de 10 alunos. Em seguida,
# desenvolva um método que solicite a altura, e o código da matrícula de cada aluno,
# armazenando em listas paralelas. Por fim, mostre a altura e o código da matrícula, do
# aluno mais alto, e do aluno mais baixo.

turma = ["Davison", "Levi", "Andre", "Anderson", "Luizao", "Fernando", "Wesley"]
alturas = []
matriculas = []

def solicitarAltura():

    for i in turma:
        altura = float(input(f"Informe a altura do {i}: "))
        alturas.append(altura)

        matricula = int(input(f"Informe a matricula do {i}: "))
        matriculas.append(matricula)


    if max(alturas):
        inh = max(alturas)
        index = alturas.index(inh)
        print(f"O aluno mais alto mede {max(alturas)} - Matricula: {matriculas[index]}")

    if min(alturas):
        inh = min(alturas)
        index = alturas.index(inh)
        print(f"O aluno mais baixo mede {min(alturas)} - Matricula:{matriculas[index]}")


solicitarAltura()
