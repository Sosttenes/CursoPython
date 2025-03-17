# Aprovação de empréstimo
emprestimo = float(input('Valor do empréstimo: R$'))
salario = float(input('Valor do seu salário: R$'))
anos = int(input('Quantidade de anos: '))
parcela = (emprestimo/anos)/12
porcentagem = salario*0.3
if parcela > porcentagem:
    print('Recusado!')
else:
    print('Aprovado!')
print(f'O valor da parcela será de {parcela:.2f}')
