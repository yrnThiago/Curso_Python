from datetime import date
cont = 0
cont2 = 0
atual = date.today().year
for n in range(1, 8):
    a = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(n)))
    idade = atual - a
    if idade > 17:
        cont += 1
    else:
        cont2 += 1
print('{} pessoas são maiores de idade!'.format(cont))
print('{} pessoas são maiores de idade!'.format(cont2))