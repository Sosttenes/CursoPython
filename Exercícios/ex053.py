# Palíndromo
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
semEspaco = ''.join(frase)
inverso = ''
for l in range(len(semEspaco) - 1, -1, -1):
    inverso += semEspaco[l]
print(inverso)
if inverso == semEspaco:
    print('É palíndromo')
else:
    print('Não é palíndromo')
