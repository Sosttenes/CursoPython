# Soma dos pares 
s = 0
for sm in range(0, 7):
    num = int(input('Digite um valor para a soma: '))
    if num % 2 == 0:
        s += num
print(s)
