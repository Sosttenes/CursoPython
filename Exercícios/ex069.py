# Tela de cadastro
homens = mulheres = maiordeIdade = 0
while True:
    print('Cadastro de Pessoas')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in "MF":
        sexo = str(input('Adicione um sexo válido [M/F]: ')).upper().strip()[0]
    cond = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while cond not in "SN":
        cond = str(input('Por favor, digite um opção válida: ')).upper().strip()[0]
    if idade > 18:
        maiordeIdade += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres += 1
    if cond == "N":
        break
print(f'Total de pessoas maiores de idade igual á {maiordeIdade}')
print(f'A o todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
