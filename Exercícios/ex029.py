# Radar eletrônico - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Digite a velocidade do carro: ')) # Pede a velocidade do carro
if velocidade > 80.0: # Se a velocidade for maior que 80
    valorMulta = (velocidade - 80.0) * 7.0 # Calcula o valor da multa
    print(f'Você excedeu o limite de velocidade, sua multa custa R${valorMulta:.2f}.') # Mostra o valor da multa
else: # Senão
    print('Você não excedeu o limite de velocidade!') # Mostra que não excedeu
# O que aprendi na aula de hoje:
# 1. Aprendi a usar a estrutura condicional if e else
# 2. Aprendi a usar operadores de comparação
# 3. Aprendi a usar operadores aritméticos
