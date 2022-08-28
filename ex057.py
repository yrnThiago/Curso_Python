'''while True:
    sexo = str(input('Qual o seu sexo? (M/F) ')).upper()
    if sexo == 'M':
        print('Seu sexo é Masculino!')
        break
    elif sexo == 'F':
        print('Seu sexo é Feminino!')
        break
    else:
        print('Opção inválida! Digite M para Masculino ou F para Feminino!')'''

sexo = ' '
while sexo not in 'MF':
    sexo = str(input('Qual o seu sexo? (M/F) ')).upper()
    if sexo not in 'MF':
        print('Opção inválida! Tente novamente!')
