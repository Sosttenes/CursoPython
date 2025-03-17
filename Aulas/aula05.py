# Condições Aninhadas
'Exercícios 36 até 45'

# Condições aninhadas são estruturas condicionais dentro de outras estruturas condicionais
# Da forma simples é escrita com "elif" que se torna uma terceira alternativa pro código que antes só tinha "if" e "else"
nome = str(input('Qual seu nome? ')).capitalize().strip()
if nome == 'Enos': # Obrigatório em todos os casos
    print('Aprovado!')
elif nome == 'Rhavi': # Ao invés de ter somente duas soluções, podemos acrescentar um caminho a mais
    print('Solicite permissão!')
else: # Opcional em todos os casos
    print('Recusado!')
# Neste exemplo podemos ver que o proprietário é Enos, e a única pessoa que tem permissão além dele é Rhavi, então ou Enos acessa, ou concede permissão pra Rhavi, ou se for outra pessoa é recusado!
