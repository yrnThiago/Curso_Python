matriz = [[], [], []]
for n in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{n, c}]: '))
        matriz[n].append(valor)
for m in matriz:
    for b in m:
        print(f'[{b:^5}]', end=' ')
    print()
5