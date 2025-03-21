# Menu
opc = 0
while opc != 5:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro valor: '))
    print('''OPÇÕES:
          [1] SOMAR
          [2] MULTIPLICAR
          [3] MAIOR
          [4] NOVOS NÚMEROS
          [5] SAIR DO PROGRAMA''')
    opc = int(input('Digite a Opção: '))
    if opc == 1:
        print(f'A soma entre {num1} + {num2} é {num1 + num2}')
    elif opc == 2:
        print(f'A multiplicação entre {num1} x {num2} é {num1*num2}')
    elif opc == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior entre {num1} e {num2} é {maior}')
    elif opc == 4:
        print('Leia os números novamente!')
    elif opc == 5:
        print('FIM DO PROGRAMA!')
    else:
        print('Opção inválida, tente novamente')
