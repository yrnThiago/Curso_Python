n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1,):
    if n % c == 0:
        print('\033[32m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n, t))
if t == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é PRIMO')

