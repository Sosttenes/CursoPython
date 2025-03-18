# Jogo de pedra, papel, tesoura
from random import randint
from time import sleep

print('-'*30)
jogador = int(input('''Escolha um:
                [1] PEDRA 🪨
                [2] PAPEL 🧻
                [3] TESOURA ✂️
                '''))
maquina = randint(1, 3)
if jogador > 3:
    print('Jogada inválida!')
print('JO')
sleep(0.3)
print('kEN')
sleep(0.4)
print('PO')
sleep(0.2)
if jogador == maquina:
    if jogador == 1:
        opc = '🪨'
    elif jogador == 2:
        opc = '🧻'
    elif jogador == 3:
        opc = '✂️'
    print(f'Empatamos! Nós escolhemos {opc}')
elif jogador == 1 and maquina == 2:
    print(f'Eu ganhei! Você escolheu 🪨  e eu 🧻')
elif jogador == 1 and maquina == 3:
    print('Você ganhou! Você escolheu 🪨  e eu ✂️')
elif jogador == 2 and maquina == 1:
    print('Você ganhou! Você escolheu 🧻  e eu 🪨')
elif jogador == 2 and maquina == 3:
    print('Eu ganhei! Você escolheu 🧻  e eu ✂️')
elif jogador == 3 and maquina == 1:
    print('Eu ganhei! Você escolheu ✂️  e eu 🪨')
elif jogador == 3 and maquina == 2:
    print('Você ganhou! Você escolheu ✂️  e eu 🧻')
