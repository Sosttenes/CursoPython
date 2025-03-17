# Alistamento militar
from datetime import date
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
alistamento = nascimento + 18
if idade > 18:
    print(f'Seu ano de alistamento foi {alistamento}, há {date.today().year-alistamento} anos!')
elif idade == 18:
    print(f'Seu alistamento será esse ano!')
else:
    print(f'Seu alistamento será em {alistamento}, daqui há {abs(date.today().year-alistamento)}anos')
