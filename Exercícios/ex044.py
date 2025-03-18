# Gerenciador de pagamentos
print(f'{' BEM VINDO! ':=^40}')
preco = float(input('Valor: R$'))
print('''FORMAS DE PAGAMENTO
      [1] à vista no dinheiro
      [2] à vista no cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
pagamento = int(input('Qual método de pagamento? '))
if pagamento == 1:
    preco = preco - preco*10/100
    print(f'Você obteve 10% de desconto, valor atual: R${preco:.2f}')
elif pagamento == 2:
    preco = preco - preco*5/100
    print(f'Você obteve 5% de desconto, valor atual: R${preco:.2f}')
elif pagamento == 3:
    preco = preco
    print(f'Valor atual: R${preco:.2f}, em duas vezes de {preco/2:.2f}')
else:
    preco = preco + preco*20/100
    totparcela = int(input('Quantas parcelas? '))
    print(f'Valor atual: R${preco:.2f}, em {totparcela} vezes de {preco/totparcela:.2f}')
