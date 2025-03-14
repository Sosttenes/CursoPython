# Sorteio
from random import choice # A função choice() escolhe um item aleatório de uma lista
a = str(input('Digite o nome do primeiro aluno: ')) # Pega o nome do primeiro aluno
b = str(input('Digite o nome do segundo aluno: ')) # Pega o nome do segundo aluno
c = str(input('Digite o nome do terceiro aluno: ')) # Pega o nome do terceiro aluno
d = str(input('Digite o nome do quarto aluno: ')) # Pega o nome do quarto aluno
l = [a, b, c, d] # Cria uma lista com os nomes dos alunos
print(f'O aluno sorteado foi {choice(l)}') # Mostra o aluno sorteado
# O que aprendi na aula de hoje:
# 1. Aprendi a usar a função choice() da biblioteca random
# 2. Aprendi a escolher um item aleatório de uma lista
# 3. Aprendi a criar uma lista
