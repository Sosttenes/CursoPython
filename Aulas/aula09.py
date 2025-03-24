# Variáveis compostas: Tuplas
'Exercícios 72 até 77'

# TUPLAS SÃO IMUTÁVEIS: desde que eu atribuia um valor para uma tupla não dá pra mudar. Só se eu parar o programa e mudar manualmente.
# Tuplas são um tipo de variável que recebem mais de um valor sem que o valor anterior seja excluído do espaço da memória como acontece na variável simples.
# Exemplo de variável simples:
lanche = 'Hambúrguer'
lanche = 'suco' 
print(lanche) # Vai imprimir "suco" pois ele tomou o lugar de "Hambúguer".
# Exemplo de tupla:
lanche = ('suco', 'hambúrguer', 'pizza', 'pudim') # Tuplas são com parêntese.
# Para acessar um valor específico dentro de uma tupla é necessário usar o fatiamento, aquele que foi visto na "aula 03" que trata sobre cadeia de caracteres. Um nome "Enos" por exemplo é uma cadeia de caracteres mas também pode se estabelecer como uma variável composta já que cada letra ocupa um espaço na memória.
print(lanche)
print(lanche[1]) # Vai imprimir o hambúrguer.
# Para acessar quantos elementos temos na tupla usamos a função len().
print(len(lanche)) # Vai imprimir o tamanho da tupla = 4.
# Se eu quiser imprimir todos os valores dentro da variável composta de uma maneira mais organizada e formatada eu uso um loop com a função de imprimir.
for comida in lanche: # O laço vai acontecer dentro da variável composta.
    print(comida) # comida vai assumir os valores dentro da variável composta.
    # Um problema que surge com essa técnica é que não podemos enumerar os itens, podemos resolver de duas maneiras.
for cont in range(0, len(lanche)): # Usamos um contador tanto para acessar a posição como para escrever ela.
    print(cont, lanche[cont]) # Vai imprimir a comida e a posição dela.
# Ou também usamos o enumerate, que vai enumerar os valores.
for pos, comida in enumerate(lanche): # O pos tá ligado como o enumerate e o comida com o lanche.
    print(pos, comida)
# Para colocar em ordem alfanúmerica eu uso a funcionalidade sorted:
print(sorted(lanche)) # Imprime lanche em ordem
del(lanche) # Vai deletar lanche da memória
