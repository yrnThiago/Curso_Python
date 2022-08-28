matriz = [[], [], []]
soma = somat = 0
for n in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{n, c}]: '))
        matriz[n].append(valor)
        if c == 2:
            somat += valor
        if valor % 2 == 0:
            soma += valor
maior = max(matriz[1])
for m in matriz:
    for b in m:
        print(f'[{b:^5}]', end=' ')
    print()
print('=-' * 20)
print(f'A soma dos valores pares é igual a {soma}')
print(f'A soma dos valores da terceira coluna é igual a {somat}')
print(f'O maior valor da segunda linha é {maior}')
