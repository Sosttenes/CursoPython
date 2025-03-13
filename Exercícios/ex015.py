# Aluguel de carros
# Descrição: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
# Distância percorrida
km = float(input('Digite a quantidade de km percorridos: ')) # Pega a quantidade de km percorridos
# Dias alugados
d = int(input('Digite a quantidade de dias alugados: ')) # Pega a quantidade de dias alugados
# Preço a pagar
p = d*60+km*0.15 # Calcula o preço a pagar
print(f'O preço a pagar é de R${p:.2f}') # Mostra o preço a pagar
# O que aprendi na aula de hoje:
# 1. Aprendi a calcular o preço de um aluguel de carro
# 2. Aprendi a usar o operador de multiplicação
# 3. Aprendi a usar o operador de soma
# 4. Aprendi a usar o operador de divisão
# 5. Aprendi a usar o operador de subtração
