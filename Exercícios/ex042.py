# Analisando triângulos V2.0
n1 = float(input('1° Reta: '))
n2 = float(input('2° Reta: '))
n3 = float(input('3° Reta: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    if n1 == n2 == n3:
        print('Triângulo equilátero')
    elif n1 != n2 != n3:
        print('Triângulo escaleno')
    else:
        print('Triângulo isóceles')
else:
    print('Não se pode formar triângulo')
