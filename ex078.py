valores = list()
pos = m = mm = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {pos}: ')))
    pos += 1
    if v == 0:
        m = mm = valores[v]
    else:
        if valores[v] > m:
            m = valores[v]
        if valores[v] < mm:
            mm = valores[v]
print('-=' * 20)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {m} nas posições ', end='')
for i, c in enumerate(valores):
    if c == m:
        print(f'{i},  ', end='')
print()
print(f'O menor valor digitado foi {mm} nas posições ', end='')
for i, c in enumerate(valores):
    if c == mm:
        print(f'{i},  ', end='')
print()