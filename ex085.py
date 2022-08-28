numeros = [], []
for n in range(1, 8):
    num = int(input(f'Digite o {n}o. valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        if num % 2 == 1:
            numeros[1].append(num)
print('=-' * 20)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')