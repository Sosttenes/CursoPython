# Primeiro e último nome de uma pessoa
name = str(input('Digite seu nome completo: ')).strip().title()
firstname = name.find(' ')
lastname = name.rfind(' ')
print(f'Seu primeiro nome é {name[:firstname]}')
print(f'Seu último nome é {name[lastname + 1:]}')
# O que aprendi na aula de hoje:
# 1. Aprendi a usar o método find() para encontrar a primeira posição de um caractere em uma string
# 2. Aprendi a usar o método rfind() para encontrar a última posição de um caractere em uma string
