# Soma de ímpares múltiplos de 3
sum = 0
for s in range(1, 501, 2):
    if s % 3 == 0:
        sum += s
print(sum)
