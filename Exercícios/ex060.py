# Cálculo de fatorial
# Maneira simples
from math import factorial
n = int(input('Digite um número: '))
fatorial = factorial(n)
print(fatorial)
# Maneira complicada
num = int(input('Digite um número: '))
cont = num 
f = 1
print(f'{num}! = ', end='')
while cont > 0:
    print(f'{cont}', end=' ')
    print('x ' if cont > 1 else'= ', end='')
    f *= cont
    cont -= 1
print(f)
