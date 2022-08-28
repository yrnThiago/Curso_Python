n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
while True:
    r = int(input('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa '''))
    if r == 1:
        s = n1 + n2
        print('A soma dos números {} e {} é igual a {}. '.format(n1, n2, s))
    elif r == 2:
        s = n1 * n2
        print('{} x {} é igual a {}. '.format(n1, n2, s))
    elif r == 3:
        if n2 > n1:
            maior = n2
        else:
            maior = n1
        print('O maior número é {}. '.format(maior))
    elif r == 4:
        print('Você escolheu novos números ..')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite mais um número: '))
    elif r == 5:
        print('Cya u later <3')
        break



