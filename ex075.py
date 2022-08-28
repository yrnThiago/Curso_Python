tabela = ((int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: '))))
print('Você digitou os valores: ', end='')
print(tabela)
nove = tabela.count(9)
if nove > 0:
    print(f'O valor 9 apareceu {nove} vezes. ')
else:
    print('O valor 9 não apareceu nenhum vez. ')
if 3 in tabela:
    tres = tabela.index(3, 0)
    print(f'O valor 3 apareceu na {tres+1}ª posição ')
else:
    print('O valor 3 não apareceu em nenhuma posição')
print('Os números pares foram: ', end='')
for n in tabela:
    if n % 2 == 0:
        print(n, end=' ')
