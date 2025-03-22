# Analisador de Strings
from time import sleep 
name = str(input('Digite seu nome completo: ')).strip().title()
print('Analisando seu nome...')
space = name.find(' ')
sleep(0.3)
print(f'Seu nome em Maiúsculas é {name.upper()}')
print(f'Seu nome em Minúsculas é {name.lower()}')
print(f'Seu nome tem ao todo {len(name) - name.count(" ")} letras')
print(f'Seu primeiro nome é {name[:space]}')
