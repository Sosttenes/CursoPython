# Pintando parede
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
# Área da parede
l = float(input('Digite a largura da parede em metros: ')) # Pega a largura da parede
a = float(input('Digite a altura da parede em metros: ')) # Pega a altura da parede
ar = l*a # Calcula a área da parede
t = ar/2 # Calcula a quantidade de tinta necessária para pintar a parede
print(f'A área da parede é de {ar:.2f}m² e a quantidade de tinta necessária para pintá-la é de {t:.2f} litros')
# O que aprendi na aula de hoje:
# 1. Aprendi a calcular a área de uma parede
# 2. Aprendi a calcular a quantidade de tinta necessária para pintar uma parede
# 3. Aprendi a usar o :.2f para mostrar duas casas decimais
# 4. Aprendi a usar a função float para transformar o valor em número real
