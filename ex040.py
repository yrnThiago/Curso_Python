nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
média = (nota1 + nota2) / 2
if média < 5.0:
    print('Sua média foi de: {}'.format(média))
    print('Você foi \033[1;31mREPROVADO\033[1m! ')
elif média < 7.0:
    print('Sua média foi de: {}'.format(média))
    print('Você está de \033[1;33mRECUPERAÇÃO\033[1m!')
else:
    print('Sua média foi de: {}'.format(média))
    print('Você foi \033[1;32mAPROVADO\033[1m!')
