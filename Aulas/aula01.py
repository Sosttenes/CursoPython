# Primitivos e Saídas
'Exercícios 03 e 04'

n1 = input('Digite um número: ') # a mensagem tem que estar entre aspas, simples sou duplas
# criamos uma variável que recebe o valor de um input
'Variável: Espaço na memória que armazena alguma informação'
'Input: Funcionalidade que abre espaço para que o usuário digite algo, dentro do parêntese se coloca a frase desejada'

n2 = input('Digite outro número: ')
soma = n1 + n2 # Nessa variável recebe o valor de n1 mais o valor de n2
print(f'A soma vale {soma}') ; 'Print = imprime na tela o que estiver entre parêntese, ou seja, o paramêtro'
# Quando eu adiciono o "f" no print eu abro o espaço para colocar uma variável ou alguma operação com as {}

print('-' *30)

# Se você executar o programa vai ver que dá errado essa conta, isso porque o programa pegou o que estava guardado na primeira
# variável e só juntou com a segunda, não somou. Isso ocorre porque quando não específicamos o tipo primitivo o Python trata ele
# como uma String ('Coisa').

n1 = int(input('Digite um número: ')) # Específiquei o tipo primitivo "int" que significa "Inteiro" ou número inteiro
n2 = int(input('Digite outro número: '))
soma = n1+n2
print(f'A soma vale {soma}')

# 4 tipos primitivos

int # Número Inteiro 
float # Número Decimal, ou com ponto flutuante
bool # Valores de verdadeiro ou falso, ou booleanos
str # Valores de varáveis "alfabéticas" tratam tudo como se fossem letras
