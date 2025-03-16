# Jogo de advinhação
from random import randint # Importa a função randint da biblioteca random
numero = randint(0, 5) # Gera um número aleatório entre 0 e 5
print('Pensei em número tente advinhar') 
advinhado = int(input('Digite um número: ')) # Pede um número ao usuário
# Estrutura condicional
if numero == advinhado: # Se o número gerado for igual ao número digitado
    print(f'Parabéns você disse {advinhado} e eu pensei em {numero}.') 
else: # Senão for igual
    print(f'Eu pensei em {numero} e você disse {advinhado}, tente outra vez.')
print('FIM!')
# O que aprendi na aula de hoje:
# 1. Aprendi a importar uma função específica de uma biblioteca
# 2. Aprendi a usar a função randint da biblioteca random
# 3. Aprendi a usar a estrutura condicional if e else
