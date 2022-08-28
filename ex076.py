lista = ('Pão', 10.00, 'Frango', 11.50, 'Presunto', 5.75)
print('==' * 20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('==' * 20)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('==' * 20)