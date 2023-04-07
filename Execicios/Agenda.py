from datetime import date

class Agenda:
    nome = ''
    data_de_nascimento = date.today()
    endereco = ''


    def __init__(self):
        self.nome = ''
        self.data_de_nascimento = date.today()
        self.endereco = ''

    def toString(self):
        print(f'nome = {self.nome} | ', end='')
        print(f'endereco = {self.endereco} | ', end='')
        print(f'data de nascimento = {self.data_de_nascimento} | ')

    def buscaContato(self):
        solicitado = print('Digite o nome do contato que deseja: ')
        print(solicitado)
