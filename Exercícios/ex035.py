# Analisador de triângulos
r1 = float(input('1° reta: '))
r2 = float(input('3° reta: '))
r3 = float(input('2° reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('É possível formar triângulo')
else:
    print('Não é possível formar triângulo')
