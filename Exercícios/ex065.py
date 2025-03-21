# Maior e menor valor MK2
maior = menor = cont = media = 0
cond = ''
while cond == 'S':
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
    media += num
    cond = input('Quer continuar? ').upper().strip()[0]
print(f'Você digitou {cont} números, e a média entre eles é de {media/cont:.2f}')
print(f'O maior valor é {maior} e o menor valor é {menor}')
