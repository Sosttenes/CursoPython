# Progressão aritmética MK2
pt = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
fim = pt + 10 * raz
while pt < fim:
    print(f'{pt}', end=' ')
    pt += raz
print('FIM!')
