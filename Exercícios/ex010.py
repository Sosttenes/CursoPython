# Conversor de moedas
r = float(input('Quanto dinheiro você tem na carteira? R$')) # Pega o valor em reais
d = r/5.38 # Converte o valor em reais para dólares
e = r/6.26 # Converte o valor em reais para euros
l = r/7.36 # Converte o valor em reais para libras
print(f'Com R${r:.2f} você pode comprar US${d:.2f}, €{e:.2f} e £{l:.2f}') # Mostra o valor convertido em dólar, euro e libra
# O que aprendi na aula de hoje:
# 1. Aprendi a fazer um conversor de moedas
# 2. Aprendi a usar o operador de divisão
# 3. Aprendi a usar o operador de formatação de strings
