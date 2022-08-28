from random import randint
cont = maior = menor = 0
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números sorteados foram : ', end='')
for s in n:
    cont += 1
    print(s, end=' ')
print('')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
