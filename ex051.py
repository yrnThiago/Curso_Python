print('=>' * 20)
print('         10 TERMOS DE UMA PA!')
print('<=' * 20)
termo = int(input('Qual o valor do primeiro termo? '))
r = int(input('Qual a sua razão? '))
décimo = termo + (10 - 1) * r
for c in range(termo, décimo + r, r):
    print('{}'.format(c), end='> ')
print('Fim')