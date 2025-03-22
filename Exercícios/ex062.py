# Progressão aritmética MK3
t = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
qtdTer = 10
fim = t + qtdTer * raz
tot = 0
while t < fim:
    print(f'{t}', end=' ')
    t += raz
while qtdTer != 0:
    qtdTer = int(input('\nQuantos termos a mais você quer?'))
    t = fim
    fim = t + qtdTer * raz
    while t < fim:
        print(f'{t}', end=' ')
        t += raz
    tot += qtdTer
print(f'\nProgressão finalizada com {tot+10} termos!')
