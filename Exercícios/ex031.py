# Custo de Viagem
distancia = float(input('Qual a distância da Viagem? '))
if distancia <= 200.00:
    preco = distancia * 0.5
    print(f'Passagem com preço de R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'Passagem com preço de R${preco:.2f}')
