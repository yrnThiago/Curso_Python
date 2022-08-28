num = int(input('Digite um valor inteiro: '))
print('''Escolha uma das bases de conversão:
\033[1;30m[1]\033[1m Converter para \033[1;30mBINÁRIO\033[1m
\033[1;30m[2]\033[1m Converter para \033[1;30mOCTAL\033[1m
\033[1;30m[3]\033[1m Converter para \033[1;30mHEXADECIMAL\033[1m''')
opção = int(input('Qual a sua opção? '))
if opção == 1:
    print('O número \033[1;30m{}\033[m convertido para \033[1;30mBINÁRIO\033[m é igual a \033[1;30m{}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número \033[1;30m{}\033[m convertido para \033[1;30mOCTAL\033[m é igual a \033[1;30m{}'.format(num, oct(num)[2]))
elif opção == 3:
    print('O número \033[1;30m{}\033[m convertido para \033[1;30mHEXADECIMAL\033[m é igual a \033[1;30m{}'.format(num, hex(num)[2]))
else:
    print('\033[1;31mOpção inválida!\033[m \033[1mTente novamente.\033[m')