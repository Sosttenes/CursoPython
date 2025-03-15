# Analisador de Strings
from time import sleep # Importa a função sleep da biblioteca time para dar um delay na execução do programa
name = str(input('Digite seu nome completo: ')).strip().title() # Recebe o nome do usuário, remove os espaços inúteis e coloca a primeira letra de cada palavra em maiúscula
print('Analisando seu nome...')
space = name.find(' ') # Encontra o primeiro espaço no nome do usuário
sleep(0.3) # Delay de 0.3 segundos
print(f'Seu nome em Maiúsculas é {name.upper()}') # Imprime o nome do usuário em maiúsculas
print(f'Seu nome em Minúsculas é {name.lower()}') # Imprime o nome do usuário em minúsculas
print(f'Seu nome tem ao todo {len(name) - name.count(" ")} letras') # Imprime a quantidade de letras do nome do usuário
print(f'Seu primeiro nome é {name[:space]}') # Imprime o primeiro nome do usuário
# O que aprendi na aula de hoje:
# 1. Aprendi a usar o método strip() para remover espaços inúteis
# 2. Aprendi a usar o método title() para colocar a primeira letra de cada palavra em maiúscula
# 3. Aprendi a usar o método find() para encontrar a posição de um caractere em uma string
# 4. Aprendi a usar o método upper() para colocar uma string em maiúsculas
# 5. Aprendi a usar o método lower() para colocar uma string em minúsculas
# 6. Aprendi a usar o método count() para contar a quantidade de vezes que um caractere aparece em uma string
# 7. Aprendi a usar o método len() para contar a quantidade de caracteres em uma string
# 8. Aprendi a usar o método slicing para pegar uma parte de uma string
# 9. Aprendi a usar a função sleep() da biblioteca time para dar um delay na execução do programa
