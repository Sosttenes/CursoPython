# Primeira e última ocorrência de uma string
name = str(input('Digite seu nome completo: ')).strip().upper()
print(f'A letra A aparece {name.count('A')} vezes')
print(f'A primeira letra A apareceu na posição {name.find('A') + 1}')
print(f'A última letra A apareceu na posição {name.rfind('A') + 1}')
