# Analisador completo:
mulheresMenores = media = idadeHomem = 0
homemVelho = ''
for p in range(1, 5):
    nome = str(input('Qual seu nome? ')).title().strip()
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? ')).upper().strip()[0]
    media += idade/4
    if idade < 20 and sexo == "F":
        mulheresMenores += 1
    if sexo == "M":
        if idade > idadeHomem:
            idadeHomem = idade
            homemVelho = nome
print(f'O homem mais velho é: {homemVelho} e tem {idadeHomem} anos')
if mulheresMenores > 1:
    print(f'Temos {mulheresMenores} mulheres menores de idade')
elif mulheresMenores == 1:
    print(f'Temos {mulheresMenores} mulher menor de idade')
else:
    print(f'Não temos mulheres menores de idade')
print(f'A média de idade do grupo é {media}')
