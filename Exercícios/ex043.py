# Cálculo de IMC
peso = float(input('Peso em KG: '))
altura = float(input('Altura em m: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Abaixo do peso! imc={imc:.2f}')
elif imc < 25:
    print(f'Peso ideal! imc={imc:.2f}')
elif imc < 30:
    print(f'Sobrepeso! imc={imc:.2f}')
elif imc < 40:
    print(f'Obesidade! imc={imc:.2f}')
else:
    print(f'Obesidade mórbida! imc={imc:.2f}')
