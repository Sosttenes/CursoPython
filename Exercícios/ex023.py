# Separando dígitos de um número
from math import trunc
num = float(input('Digite um número de 0 a 9999: '))
u = (num // 1) % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000) % 10
print(f'Unidade: {trunc(u)}\nDezena: {trunc(d)}\nCentena: {trunc(c)}\nMilhar: {trunc(m)}')
