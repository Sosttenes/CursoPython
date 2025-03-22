# Estátistica de produto
menor = soma = maior = cont = 0
nome = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cond = ' '
    while cond not in "SN":
        cond = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma += preco
    cont += 1
    if preco > 1000:
        maior += 1
    if cont == 1 or preco < menor:
        menor = preco
        nome = produto
    if cond == "N":
        break
print(f'''O total da compra foi de R${soma:.2f}
Temos {maior} produto custando mais de R$1.000,00
O produto mais barato foi {nome} que custou R${menor}''')
