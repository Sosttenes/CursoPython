# Validador de dados
sexo = str(input('Digite seu sexo: [F/M] ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Inválido, por favor tente novamente: ')).upper().strip()[0]
if sexo == 'F':
    print('Sexo feminino')       
else:
    print('Sexo masculino')
print('FIM!')
