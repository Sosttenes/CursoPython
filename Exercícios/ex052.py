# Números primos
num = int(input('Digite um número: '))
div = 0
for p in range(1, num+1):
    if num % p == 0:
        print('\033[32m', end=' ')
        div += 1
    else:
        print('\033[33m', end=' ')
    print(p, end= ' ')
print('\033[0m')
if div == 2:
    print('\033[032m É divisível')
else:
    print('\033[31m Não é divisível')
print('\033[0m')
