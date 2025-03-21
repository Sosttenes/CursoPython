# Tabuada MK3
while True:
    num = int(input('Qual tabuada você quer ver? '))
    if num < 0:
        break
    for t in range(0, 11):
        print(f'{num} x {t:>2} = {num*t}')
