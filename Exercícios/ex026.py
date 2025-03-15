# Primeira e última ocorrência de uma string
name = str(input('Digite seu nome completo: ')).strip().upper() # Recebe o nome do usuário, remove os espaços inúteis e coloca todas as letras em maiúsculas
print(f'A letra A aparece {name.count('A')} vezes') # Verifica quantas vezes a letra A aparece no nome do usuário
print(f'A primeira letra A apareceu na posição {name.find('A') + 1}') # Verifica a primeira posição em que a letra A aparece
print(f'A última letra A apareceu na posição {name.rfind('A') + 1}') # Verifica a última posição em que a letra A aparece
# O que aprendi na aula de hoje:
# 1. Aprendi a usar o método count() para contar a quantidade de vezes que um caractere aparece em uma string
# 2. Aprendi a usar o método find() para encontrar a primeira posição de um caractere em uma string
# 3. Aprendi a usar o método rfind() para encontrar a última posição de um caractere em uma string
