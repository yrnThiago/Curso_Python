from datetime import date
a = int(input('Qual ano quer analisar? Digite 0 para o ano atual: : '))
if a == 0:
    a = date.today().year
print('Analisando o ano {}..'.format(a))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('{} é um ano bissexto'.format(a))
else:
    print('{} não é um ano bissexto'.format(a))
