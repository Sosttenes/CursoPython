# Separando dígitos de um número
from math import trunc # Importa a função trunc da biblioteca math
num = float(input('Digite um número de 0 a 9999: ')) # Pede um número ao usuário
u = (num // 1) % 10 # Pega a unidade do número 
d = (num // 10) % 10 # Pega a dezena do número
c = (num // 100) % 10 # Pega a centena do número
m = (num // 1000) % 10 # Pega o milhar do número
print(f'Unidade: {trunc(u)}\nDezena: {trunc(d)}\nCentena: {trunc(c)}\nMilhar: {trunc(m)}') # Imprime a unidade, dezena, centena e milhar do número
# O que aprendi na aula de hoje:
# 1. Aprendi a usar a função trunc() da biblioteca math para pegar a parte inteira de um número
# 2. Aprendi a usar o operador // para pegar a parte inteira de um número
# 3. Aprendi a usar o operador % para pegar o resto da divisão de um número
