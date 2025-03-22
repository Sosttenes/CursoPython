# Radar eletrônico
velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80.0:
    valorMulta = (velocidade - 80.0) * 7.0
    print(f'Você excedeu o limite de velocidade, sua multa custa R${valorMulta:.2f}.')
else:
    print('Você não excedeu o limite de velocidade!')
