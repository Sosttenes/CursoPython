# Progressão aritmética MK3
t = int(input('Digite o primeiro termo: ')) # O usuário coloca o primeiro termo
raz = int(input('Digite a razão: ')) # O usuário coloca a razão
qtdTer = 10 # Variável que indica a quantidade de termos
fim = t + qtdTer * raz # Cálculo para o fim da PA, neste caso com 10 termos
tot = 0
while t < fim:
    print(f'{t}', end=' ') # Imprime o valor do termo
    t += raz # Adiciona a razão no termo anterior pra que chege no fim do laço
while qtdTer != 0: # Laço para validar se o Usuário quer continuar ou não vendo os termos
    qtdTer = int(input('\nQuantos termos a mais você quer?')) # Validação se for 0 acaba o programa
    t = fim # O valor dado para o fim da primeira PA se tornará o primeiro termo da segunda
    fim = t + qtdTer * raz # Cálculo com a nova quantidade de termos
    while t < fim:
        print(f'{t}', end=' ')
        t += raz
    tot += qtdTer
print(f'\nProgressão finalizada com {tot+10} termos!')
