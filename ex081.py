valores = list()
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    r = str(input('Quer continuar? (S/N) ')).upper()
    if r in 'N':
        break
    else:
        if r not in 'SN':
            print('Comando incorreto! Digite S para continuar ou N para parar..')
            r = str(input('Quer continuar? (S/N) ')).upper()
            if r in 'N':
                break
print('-=' * 20)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem crescente são {sorted(valores)}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')

