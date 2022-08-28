print('==' * 20)
print('      BANCO CAPITALISTA MALVADÃO')
print('==' * 20)
valor = int(input('Qual valor você deseja sacar? R$'))
while True:
    nota50 = valor // 50
    resto = valor % 50
    print(f'{nota50} cédulas de 50 Reais.')
    if resto != 0:
        nota20 = resto // 20
        resto = valor % 20
        print(f'{nota20} cédulas de 20 Reais.')
        if resto != 0:
            nota10 = resto // 10
            resto = valor % 10
            print(f'{nota10} cédulas de 10 Reais.')
            if resto != 0:
                nota1 = resto // 1
                print(f'{nota1} cédulas de 1 Real.')
    break
