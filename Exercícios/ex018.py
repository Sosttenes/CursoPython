# Seno, cosseno e tangente de um ângulo
# Descrição: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan
a = float(input('Digite um ângulo: ')) # Pega um ângulo
s = sin(a) # Calcula o seno
c = cos(a) # Calcula o cosseno
t = tan(a) # Calcula a tangente
print(f'O seno de {a} é {s:.2f}, o cosseno é {c:.2f} e a tangente é {t:.2f}') # Mostra o seno, cosseno e tangente
# O que aprendi na aula de hoje:
# 1. Aprendi a usar a função sin() da biblioteca math
# 2. Aprendi a usar a função cos() da biblioteca math
# 3. Aprendi a usar a função tan() da biblioteca math
