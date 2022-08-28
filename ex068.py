from random import randint
cont = 0
print('->' * 20)
print('       VAMOS JOGAR PAR OU ÍMPAR ')
print('<-' * 20)
while True:
    v = int(input('Digite um valor: '))
    c = randint(0, 10)
    r = v + c
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? (P/I) ')).strip().upper()[0]
        print('-' * 40)
        print(f'Você jogou {v} e o computador escolheu {c}. Total = {v + c} ', end='')
        print('(PAR)' if r % 2 == 0 else '(ÍMPAR)')
        print('-' * 40)
    if tipo == 'P':
        if r % 2 == 0:
            p = 'PAR'
            cont += 1
            print('Você VENCEU!')
            print('=-' * 20)
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if r % 2 == 1:
            i = 'ÍMPAR'
            cont += 1
            print('Você VENCEU!')
            print('=-' * 20)
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes. ')