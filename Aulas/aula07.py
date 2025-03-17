# Estrutura de repetição While
'Exercícios 57 até 65'

# Quando não tivermos os parâmetros definidos por número ou não sabemos quais são, o laço "for" vai se tornar obsoleto, pra isso temos a estrutura de repetição "while", que significa "enquanto". Logo após usamos a condição pra que o loop seja interrompido e pare de repetir.
# Em termos técnicos o while é chamado de estrutura de repetição por teste lógico.
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM!')
# Este mesmo exemplo foi usado na aula passada
r = 'S' # Essa vai ser a minha condição inicial para que o loop seja executado
while r == 'S': # Início do loop com a condição de cima validada
    num = int(input('Digite um valor: '))
    r = str(input('Quer continuar: '))[0].upper() # Vai pegar somente a primeira letra e colocar pra maiúscula caso não esteja, essa variável vai definir o fim ou a continuação do loop
