# Sequência de Fibonacci
numTermos = int(input('Quantos termos você quer ver? '))
cont = 3
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
while cont < numTermos:
    t3 = t1 + t2
    print(f'{t3}', end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
