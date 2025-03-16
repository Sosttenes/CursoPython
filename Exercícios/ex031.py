# Custo de Viagem - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
distancia = float(input('Qual a distância da Viagem? ')) # Pede a distância da viagem
if distancia <= 200.00: # Se a distância for menor ou igual a 200
    preco = distancia * 0.5 # Calcula o preço da passagem
    print(f'Passagem com preço de R${preco:.2f}') # Mostra o preço da passagem
else: # Senão
    preco = distancia * 0.45 # Calcula o preço da passagem
    print(f'Passagem com preço de R${preco:.2f}') # Mostra o preço da passagem
# O que aprendi na aula de hoje:
# 1. Aprendi a usar a estrutura condicional if e else
# 2. Aprendi a usar operadores de comparação
# 3. Aprendi a usar operadores aritméticos
