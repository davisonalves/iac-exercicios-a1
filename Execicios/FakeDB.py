import csv

from Contato import Contato
from Agenda import Agenda

from datetime import datetime
from datetime import date

class FakeDB:

    Contatos = []
    Agendas = []

    def auto_fill_contatos(self):
        with open('contato.txt') as csvfile:
            linereader = csv.reader(csvfile, delimiter=',')
            for row in linereader:
                obj = Contato()
                obj.email = row[1]
                obj.telefone = row[2]
                self.Contatos.append(obj)

    def auto_fill_agenda(self):
        with open('contato.txt') as csvfile:
            linereader = csv.reader(csvfile, delimiter=',')
            for row in linereader:
                obj = Agenda()
                obj.nome = row[0]
                obj.endereco = row[3]
                obj.data_de_nascimento = datetime.strptime(row[4], '%Y-%m-%d').date()
                self.Agendas.append(obj)

    def __init__(self):
        self.auto_fill_contatos()
        self.auto_fill_agenda()
