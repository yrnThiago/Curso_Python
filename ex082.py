valores = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    if num % 2 == 1:
        impares.append(num)
    r = str(input('Quer continuar? (S/N) ')).upper()
    if r in 'N':
        break
    else:
        if r not in 'SN':
            print('Comando incorreto! Digite S para continuar ou N para parar..')
            r = str(input('Quer continuar? (S/N) ')).upper()
            if r in 'N':
                break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')