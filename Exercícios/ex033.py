# Maior e menor valor
num = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
num3 = float(input('Digite o 3° número: '))
maior = menor = num
if num2 > num and num2 > num3:
    maior = num2
if num2 < num and num2 < num3:
    menor = num2
if num3 > num and num3 > num2:
    maior = num3
if num3 < num and num3 < num2:
    menor = num3
print(f'O maior número é: {maior:.1f}')
print(f'O menor número é: {menor:.1f}')
# O que aprendi na aula de hoje:
# 1. Aprendi a igualar variáveis com mesmo valor na mesma linha "maior = menor = num"
# 2. Aprendi a lógica de tomar um valor como maior e menor até que surja outro pra modificar
