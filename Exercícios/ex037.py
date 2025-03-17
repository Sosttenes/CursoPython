# Conversor de bases númericas
num = int(input('Digite um valor inteiro: '))
print('ESCOLHA UMA OPÇÃO DE CONVERSÃO'
'\n1 - HEXADECIMAL'
'\n2 - OCTAL'
'\n3 - BINÁRIO')
opc = int(input('Qual sua escolha? '))
if opc == 1:
    print(f'{num} em hexadecimal é {hex(num)[2:]}')
elif opc == 2:
    print(f'{num} em octal é {oct(num)[2:]}')
elif opc == 3:
    print(f'{num} em binário é {bin(num)[2:]}')
else:
    print(f'{opc} é um número inválido, reinicie o programa!')
