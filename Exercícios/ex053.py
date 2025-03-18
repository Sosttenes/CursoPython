# Palíndromo
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split() # Fiz uma lista com as palavras da frase
semEspaco = ''.join(frase) # Juntei todas as palavras sem espaço
inverso = ''
for l in range(len(semEspaco) - 1, -1, -1): # Vai definir a quantidade de vezes que vai se repetir a iteração e a ordem que vai acontecer
    inverso += semEspaco[l] # "semEspaco[l]" identifica a letra e adiciona ela na variável inverso, o "l" primeiro vai ser 3 depois 2...   semEspaco[3], semEspaco[2]...
print(inverso)
if inverso == semEspaco:
    print('É palíndromo')
else:
    print('Não é palíndromo')
