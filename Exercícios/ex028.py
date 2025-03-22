# Jogo de advinhação
from random import randint
numero = randint(0, 5)
print('Pensei em número tente advinhar') 
advinhado = int(input('Digite um número: '))
if numero == advinhado:
    print(f'Parabéns você disse {advinhado} e eu pensei em {numero}.') 
else:
    print(f'Eu pensei em {numero} e você disse {advinhado}, tente outra vez.')
print('FIM!')
