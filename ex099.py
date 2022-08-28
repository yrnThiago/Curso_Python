from time import sleep


def maior(* num):
    cont = maior = 0
    print('=-' * 25)
    print('Analisando os valores passados.. ')
    for m, n in enumerate(num):
        sleep(0.25)
        print(f'{n}', end=' ')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo. ')
    print(f'O maior valor informado foi {maior}. ')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


