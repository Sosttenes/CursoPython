# Ano bissexto
from datetime import date # Importa a função data da biblioteca datetime
ano = int(input('Qual ano quer analisar? Para analisara o ano atual digite 0: ')) # Pega um ano do usuário
if ano == 0: # Condição de que se o usuário pedir o número zero terá o ano atual
    ano = date.today().year # Transforma o "0" no ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Se o número for divisível por 4, e não for divisível por 100 ou for divisível por 400 ele é Bissexto
    print(f'Ano {ano} é bissexto!')
else: # Senão
    print(f'Ano {ano} não é bissexto!')
# O que aprendi na aula de hoje:
# 1. Aprendi que a biblioteca datetime importa as marcas de horário e data da máquina
# 2. Aprendi a regra de ano bissexto em linguagem lógica
