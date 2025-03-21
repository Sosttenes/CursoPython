# Cálculo de fatorial
# Maneira simples
from math import factorial
n = int(input('Digite um número: '))
fatorial = factorial(n)
print(fatorial)
# Maneira complicada
num = int(input('Digite um número: '))
cont = num # O contador vai começar sendo o mesmo valor do fatorial
f = 1 # Fatorial sendo o número 1 o valor nulo esperado para a multiplicação
print(f'{num}! = ', end='')
while cont > 0:
    print(f'{cont}', end=' ')
    print('x ' if cont > 1 else'= ', end='')
    f *= cont # Vai começar multiplicando o 1 que tá fora do laço pelo primeiro termo, ou seja, pelo num e vai refredindo conforme o loop vai sendo passado pelo "cont -= 1". 
    cont -= 1 # Contador vai regressando para representar o fatorial
print(f)
