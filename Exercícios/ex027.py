# Primeiro e último nome de uma pessoa
name = str(input('Digite seu nome completo: ')).strip().title()
firstname = name.find(' ')
lastname = name.rfind(' ')
print(f'Seu primeiro nome é {name[:firstname]}')
print(f'Seu último nome é {name[lastname + 1:]}')
