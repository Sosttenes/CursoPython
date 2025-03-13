# Calculando descontos
# Descrição: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# Preço do produto
p = float(input('Digite o preço do produto: R$', )) # Pega o preço do produto
d = p*(5/100) # Calcula o desconto de 5%
np = p-d # Calcula o novo preço do produto
print(f'O preço do produto é de R${p:.2f} e com 5% de desconto, o novo preço é de R${np:.2f}')
# O que aprendi na aula de hoje:
# 1. Aprendi a calcular descontos
# 2. Aprendi a usar o operador de multiplicação
# 3. Aprendi a usar o operador de divisão
# 4. Aprendi a usar o operador de subtração
