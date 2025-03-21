# Jogo de par ou ímpar
from random import randint
cont = 0
while True:
    num = int(input('Digite um número: '))
    parouimpar = ' '
    while parouimpar not in 'PI':
        parouimpar = str(input('Escolha par ou ímpar: ')).upper().strip()[0]
    com = randint(0, 10)
    result = num + com
    if result % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'
    if parouimpar == resultado[0]:
        print(f'Você ganhou, eu joguei {com} e você {num} deu {resultado}')
        cont += 1
    else:
        print(f'Você perdeu, eu joguei {com} e você {num} deu {resultado}')
        break
print(f'GAME OVER! Você ganhou {cont} vezes')
