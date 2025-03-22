# Aluguel de carros
km = float(input('Digite a quantidade de km percorridos: '))
d = int(input('Digite a quantidade de dias alugados: '))
p = d*60+km*0.15
print(f'O preço a pagar é de R${p:.2f}')
