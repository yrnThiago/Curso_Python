casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Quantos anos deseja pagar? '))
prestação = casa / anos / 12
print('Para pagar uma casa de \033[1mR${:.2f}\033[m em \033[1m{:.0f}\033[m anos, o valor da prestação mensal é de: \033[1mR${:.2f}\033[m'.format(casa, anos, prestação))
porcentagem = salário / 100 * 30
if prestação > porcentagem:
    print('\033[1mEmpréstimo \033[1;31mNEGADO!\033[m')
else:
    print('\033[1mEmpréstimo \033[1;32mCONCEDIDO!\033[m')

