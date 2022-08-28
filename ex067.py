while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 20)
    for c in range(1, 11):
        r = n * c
        print(f'{n} x {c} = {r}', end='''
''')
    print('-' * 20)
print('Saindo do programa de tabuadas. Volte sempre! ')