'''n0 = int(input('Digite um número e obtenha a sua tabuada: '))
n1 = n0 * 1
n2 = n0 * 2
n3 = n0 * 3
n4 = n0 * 4
n5 = n0 * 5
n6 = n0 * 6
n7 = n0 * 7
n8 = n0 * 8
n9 = n0 * 9
n10 = n0 * 10
print('A tabuada para este número é: \n {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {}'.format(n0, n1, n0, n2, n0, n3), end='')
print('\n {} x 4 = {} \n {} x 5 = {} \n {} x 6 = {} \n {} x 7 = {} \n {} x 8 = {}'.format(n0, n4, n0, n5, n0, n6, n0, n7,n0, n8), end='')
print('\n {} x 9 = {} \n {} x 10 = {}.'.format(n0, n9, n0, n10))
'''


num = int(input('Digite um número e obtenha a sua tabuada: '))
for multiplicador in range(1, 10):
    print(f'{num} X {multiplicador} = {num * multiplicador}')
print(f'{num} X 10 = {num*10}.')

