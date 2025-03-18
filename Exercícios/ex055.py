# Maior e menor de uma sequência
maior = menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}° pessoa: Kg'))
    if p == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'''O maior equivale a: {maior}KG
O menor equivale a {menor}KG''')
