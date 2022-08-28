from datetime import date
ano = int(input('Qual o ano de nascimento do atleta? '))
idade = date.today().year - ano
if idade < 10:
    print('O atleta tem {} anos e faz parte da categoria: MIRIM!'.format(idade))
elif idade < 15:
    print('O atleta tem {} anos e  faz parte da categoria: INFANTIL!'.format(idade))
elif idade < 20:
    print('O atleta tem {} anos e faz parte da categoria: JUNIOR!'.format(idade))
elif idade == 20:
    print('O atleta tem {} anos e faz parte da categoria: SÊNIOR!'.format(idade))
else:
    print('O atleta tem {} anos e faz parte da categoria: MASTER!'.format(idade))
