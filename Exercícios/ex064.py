# Tratando vários valores
num = soma = cont = 0
while num != 999:
    num = int(input('Digite um valor [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
    else:
        print()
print(f'Foram digitados {cont} números, e a soma entre eles é {soma}')
