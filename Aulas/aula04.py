# Estruturas condicionais
'Exercícios 28 até 35'

# Estruturas condicionais são utilizadas para tomada de decisões com base em condições. Permitindo que o programa execute diferentes ações de acordo com o resultado da condição.
# Exemplo:
idade = int(input('Quantos anos você tem? ')) # Pede a idade do usuário
if idade >= 18: # Se a idade for maior ou igual a 18 anos, lembre-se que devemos colocar dois pontos no final da condição pra identificar o início de um bloco de código
    print('Você é maior de idade') # Imprime "Você é maior de idade"
# Primeiro bloco de código
else: # Senão for maior ou igual a 18 anos
    print('Você é menor de idade') # Imprime "Você é menor de idade"
# Segundo bloco de código
# Os blocos nunca são executados juntos, apenas um deles é executado de acordo com a condição
# Forma simplificada de escrever uma estrutura condicional
print('Você é maior de idade' if idade >= 18 else 'Você é menor de idade')
