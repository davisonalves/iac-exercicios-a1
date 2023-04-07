# POO_07 - Faça um programa de agenda telefônica, com as classes Agenda e
# Contato

class Contato:
    telefone = ''
    email = ''

    def __init__(self):
        self.telefone = ''
        self.email = ''

    def toString(self):
        print(f'telefone = {self.telefone} | ', end='')
        print(f'email = {self.email} | ')
