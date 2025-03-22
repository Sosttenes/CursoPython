# Catetos e hipotenusa
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(co, ca)
print(f'O comprimento da hipotenusa é {h:.2f}')
