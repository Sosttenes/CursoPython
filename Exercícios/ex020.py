# Sorteio de ordem
from random import shuffle # A função shuffle() embaralha os itens de uma lista
a = str(input('Digite o nome do primeiro aluno: ')) # Pega o nome do primeiro aluno
b = str(input('Digite o nome do segundo aluno: ')) # Pega o nome do segundo aluno
c = str(input('Digite o nome do terceiro aluno: ')) # Pega o nome do terceiro aluno
d = str(input('Digite o nome do quarto aluno: ')) # Pega o nome do quarto aluno
l = [a, b, c, d] # Cria uma lista com os nomes dos alunos
print(f'A ordem de apresentação será {shuffle(l)}') # Mostra a ordem de apresentação
# O que aprendi na aula de hoje:
# 1. Aprendi a usar a função shuffle() da biblioteca random
# 2. Aprendi a embaralhar os itens de uma lista
# 3. Aprendi a criar uma lista
