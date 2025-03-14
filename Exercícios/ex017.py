# Catetos e hipotenusa
# Descrição: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: ')) # Pega o comprimento do cateto oposto
ca = float(input('Digite o comprimento do cateto adjacente: ')) # Pega o comprimento do cateto adjacente
h = hypot(co, ca) # Calcula a hipotenusa
print(f'O comprimento da hipotenusa é {h:.2f}') # Mostra o comprimento da hipotenusa
# O que aprendi na aula de hoje:
# 1. Aprendi a usar a função hypot() da biblioteca math
# 2. Aprendi a calcular a hipotenusa de um triângulo retângulo
