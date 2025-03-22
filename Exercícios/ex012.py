# Calculando descontos
p = float(input('Digite o preço do produto: R$', ))
d = p*(5/100)
np = p-d
print(f'O preço do produto é de R${p:.2f} e com 5% de desconto, o novo preço é de R${np:.2f}')
