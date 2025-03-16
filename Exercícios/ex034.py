# Aumentos múltiplos de salário
sal = float(input('Digite seu salário: R$'))
if sal >= 1250.0:
    sal += sal*(10/100)
else:
    sal += sal*(15/100)
print(f'Seu salário é de: R${sal:.2f}')
