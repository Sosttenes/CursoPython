# Advinhação V2.0
from random import randint
computador = randint(0, 10)
cont = 1
print('Olá sou seu computador, acabei de pensar em um número, tente advinhar...')
eu = int(input('Qual é o seu palpite: '))
while computador != eu:
    if computador > eu:
        print('\033[034mMais... Tente outra vez!')
    else:
        print('\033[033mMenos... Tente de novo!')
    eu = int(input('\033[mQual é o seu palpite: '))
    cont += 1
print(f'\033[032mAcertou, na {cont}° tentativa')
