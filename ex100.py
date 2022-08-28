numeros = list()


def sorteia(a, b):
    from time import sleep
    from random import randint
    for v in range(0, 5):
        numeros.append(randint(a, b))
    print(f'Sorteando 5 valores da lista: ', end='')
    for n, m in enumerate(numeros):
        sleep(0.25)
        print(f'{m}', end=' ')
    print('PRONTO! ')


def somaPar(*n):
    soma = 0
    for n, m in enumerate(numeros):
        if m % 2 == 0:
            soma += m
    print(f'Somando os valores pares de {numeros}, temos {soma}. ')

sorteia(0, 10)
somaPar(*numeros)
