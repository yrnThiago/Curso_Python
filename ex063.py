print('=>' * 20)
print('        SEQUÊNCIA DE FIBONACCI')
print('<=' * 20)
t1 = 0
t2 = 1
cont = 3
t = int(input('Quantos termos você quer mostrar? '))
print(' {} > {} > '.format(t1, t2), end='')
while cont <= t:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print('{} > '.format(t3), end='')
print('FIM')
