# Verificando existência de um nome
name = str(input('Digite seu nome completo: ')).strip().title()
print(f'Seu nome tem Silva? {"Silva" in name}')
