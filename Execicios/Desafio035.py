# 35 Desenvolva um método que imprima todos os múltiplos de 3, entre 1 e 100.

print("Multiplos de 3, de 1 até 100: ")
for i in range(1, 101):
    if i % 3 == 0:
        print(i)
