nome = input('Digite o seu nome completo: ').strip()
print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))
print('Seu nome possui: {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem: {} letras'.format(nome.find(' ')))
