# Estrutura de repetição for
'Exercícios 46 até 56'

# Laços, repetições ou iterações, qualquer desses nomes definem estruturas de repetição.
# Na estrutura for temos uma iteração com variável de controle que diz quando o programa deve parar de repetir atráves de um número ou de uma contagem, como por exemplo:
for c in range(1, 11): # For é o laço, c é a variável o "in range" significa "no intervalo", e o que está dentro do parêntese é o meu parâmetro. OBS: o último número é sempre excluído, então neste caso só será escrito de 1 até 10
    print(c, end=' ') # Aqui o "c" vai assumir o valor do intervalo, ou seja, o "c" vai ser atualizado a cada vez que se repetir, o "end=' '" é pra que no final dos prints ao invés de quebrar a lniha ele acrescente um espaço
# Além dos dois parâmetros que são o início e fim, eu posso colocar o passo que isso vai acontecer, se quiser que pule de dois em dois: (1, 11, 2) se eu quiser que ele conte em regressivo: (10, -1, -1)
for c in range(10, -1, -1): # Contagem regressiva de 10 até 0
    print(c)
for c in range(0, 11, 2): # Contagem pulando de dois em dois
    print(c)
# Também posso atribuir variáveis como os parâmetros
init = int(input('Início: '))
end = int(input('Fim: '))
pas = int(input('Passo: '))
for c in range (init, end, pas):
    print(c)
# Posso também colocar as variáveis e interações dentro do laço
s = 0 # Declaro a soma = 0 fora da variável para que ele não se torne 0 toda vez que ela repetir
for c in range(0, 3):
    n = (int(input('Digite um valor: ')))
    s += n # Vai pegar o valor digitado e somar cada um a cada repetição
print(f'Soma igual á: {s}')
