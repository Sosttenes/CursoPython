# Interrompendo repetições While
'Exercícios 66 até 71'

# A condição infinta "True" faz o programa repetir infinitamente e aqui surge nosso "problema", pois o while True serve pra casos como quando você não sabe quando o usuário quer parar, como no código a seguir:
s = 0
while True: # Condição infinita
    num = int(input('Digite um valor: '))
    r = str(input('Quer continuar? ')).strip().upper()[0] # Validação de repetição ou encerramento
    s += num
    if r == 'N': # Condição de parada
        break # Instrução de parada
print(f'A soma é {s}')
