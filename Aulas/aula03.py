# Manipulação de cadeias de caracteres
'Exercícios 22 até 27'

# O que é uma cadeia de caracteres?
# Uma cadeia de caracteres é uma sequência de caracteres, como uma palavra ou uma frase.
# Em Python, uma cadeia de caracteres é representada por um objeto do tipo str.
# Uma cadeia de caracteres é delimitada por aspas simples ou duplas.
# Exemplos de cadeias de caracteres:
'Python' or "Python"
# Essa palavra ou cadeia de caracteres não vai inteira, ela vai ocupando posições na memória. o 'P' vai ocupar a posição 0, o 'y' vai ocupar a posição 1, e assim por diante.
# Com a separação de cada caractere, podemos acessar cada caractere individualmente. O que facilita a manipulação de cadeias de caracteres.

# Fatiamento de cadeias de caracteres

frase = 'Curso em vídeo python'
print(frase) # Vai imprimir a frase inteira
print(frase[3]) # Vai imprimir a letra que está na posição 3, ou seja, o "s"
# Para acessar um caractere utilizamos colchetes [] após o nome da variável que armazena a cadeia de caracteres.
print(frase[3:13]) # Vai imprimir da posição 3 até a posição 12, ou seja, "so em Víde"
# Para acessar um intervalo de caracteres utilizamos dois pontos : separando os índices inicial e final do intervalo.
print(frase[3:13:2]) # Vai imprimir da posição 3 até a posição 12, pulando de 2 em 2, ou seja, "sm í"
# Para acessar um intervalo de caracteres de uma cadeia de caracteres, com um intervalo de pulo, utilizamos outro dois pontos : separando o intervalo de pulo.
print(frase[:14]) # Vai imprimir da posição 0 até a posição 13, ou seja, "Curso em Vídeo"
print(frase[13:]) # Vai imprimir da posição 13 até o final, ou seja, "o Python"
print(frase[9:26]) # Vai imprimir até o final da frase, ou seja, "Vídeo Python"
print(frase[9::3]) # Vai imprimir da posição 9 até o final, pulando de 3 em 3, ou seja, "VdoPh"

# Análise de cadeias de caracteres

print(len(frase)) # Vai imprimir o tamanho da frase, ou seja, 21 caracteres
# len() significa "length" que em inglês significa "comprimento"
print(frase.count('o')) # Vai contar quantas vezes a letra "o" aparece na frase
print(frase.count('o', 0, 14)) # Vai contar quantas vezes a letra "o" e "O" aparece na frase, do índice 0 até o índice 13
print(frase.find('deo')) # Vai mostrar em qual posição começa a palavra "deo"
# Se a palavra não existir na frase, o Python vai retornar -1
print('Curso' in frase) # Vai mostrar se a palavra "Curso" está na frase
# O operador "in" verifica se uma palavra está contida na frase.
# O operador "not in" verifica se uma palavra não está contida na frase.

# Transformação de cadeias de caracteres

print(frase.replace('Python', 'Android'))
# O método replace() substitui uma palavra por outra em uma cadeia de caracteres.
print(frase.upper())
# O método upper() transforma todas as letras em maiúsculas.
print(frase.lower())
# O método lower() transforma todas as letras em minúsculas.
print(frase.capitalize())
# O método capitalize() transforma a primeira letra em maiúscula.
print(frase.title())
# O método title() transforma a primeira letra de cada palavra em maiúscula.
print(frase.strip())
# O método strip() remove os espaços inúteis no começo e no final da frase.
print(frase.rstrip())
# O método rstrip() remove os espaços inúteis no final da frase.
print(frase.lstrip())
# O método lstrip() remove os espaços inúteis no começo da frase.
print(frase.split())
# O método split() identifica os espaços em uma frase e separa as palavras pra colocar em uma lista. Se você colocar um parâmetro dentro dos parênteses, ele vai separar a frase por esse parâmetro. Exemplo:
print(frase.split('o')) # Vai separar a frase toda vez que existir o caracter "o"
print('-'.join(frase))
# O método join() junta os elementos de uma lista em uma cadeia de caracteres. Se você colocar um parâmetro dentro dos parênteses, ele vai juntar a lista com esse parâmetro.
