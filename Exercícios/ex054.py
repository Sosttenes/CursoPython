# Grupo de maioridade
from datetime import date
maior = menor = 0
for p in range(0, 7):
    nascimento = int(input('Qual ano você nasceu: '))
    idade = date.today().year - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade!')
print(f'{menor} pessoas são menores de idade!')
