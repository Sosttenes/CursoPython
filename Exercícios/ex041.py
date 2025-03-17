# Classificação de atletas
from datetime import date
nascimento = int(input('Qual seu ano de nascimento? '))
idade = date.today().year - nascimento
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('ATLETA MIRIM')
elif idade <= 14:
    print('ATLETA INFANTIL')
elif idade <= 19:
    print('ATLETA JÚNIOR')
elif idade <= 25:
    print('ATLETA PRO')
else:
    print('ATLETA SÊNIOR')
