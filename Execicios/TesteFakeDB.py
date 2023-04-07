from FakeDB import FakeDB

fakeDB = FakeDB()

for cont in fakeDB.Contatos:
    cont.toString()

print(100 * '-')

for agen in fakeDB.Agendas:
    agen.toString()
