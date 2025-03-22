# Sorteio de ordem
from random import shuffle
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
l = [a, b, c, d]
print(f'A ordem de apresentação será {shuffle(l)}')
