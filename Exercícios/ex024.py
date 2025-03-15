# Verificando primeiras letras de um texto
city = str(input('Digite o nome de um ciade: ')).strip().title()
print(city[:5] == 'Santa') # Verifica se as primeiras cinco letras da cidade são iguais a 'Santa'
