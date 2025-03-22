# Ano bissexto
from datetime import date
ano = int(input('Qual ano quer analisar? Para analisara o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Ano {ano} é bissexto!')
else:
    print(f'Ano {ano} não é bissexto!')
