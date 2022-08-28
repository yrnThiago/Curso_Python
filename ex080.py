valores = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Valor adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Valor adiconado na posição {pos}...')
                break
            pos += 1
print('--' * 25)
print(f'A lista em ordem crescente é {valores}')
