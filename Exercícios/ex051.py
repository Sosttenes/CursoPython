# Progressão aritmética
pt = int(input('Digite o primeiro termo da PA: '))
passo = int(input('Digite a razão: '))
for pa in range(pt, pt + 10 * passo, passo):
    print(pa, end='  ➡️  ')
print('ACABOU!')
