# Média escolar
n1 = float(input('1° Nota: '))
n2 = float(input('2° Nota: '))
n3 = float(input('3° Nota: '))
media = (n1 + n2 + n3)/3
if media >= 7.0:
    print(f'Parabéns, você está aprovado com média igual a {media:.2f}!')
elif 5.0 < media < 7.0:
    print(f'Quase lá, sua média é {media:.2f}, vai pra final!')
else:
    print(f'Sua média é {media:.2f} e você está reprovado!')
