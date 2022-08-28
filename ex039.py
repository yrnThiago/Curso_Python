from datetime import date
ano = int(input('Qual o ano do seu nascimento? '))
anoa = date.today().year
idade = anoa - ano
alistamento = 18 - idade
alistamento1 = idade - 18
print('Sua idade é de {} anos'.format(idade))
if idade < 18:
    print('Você irá se alistar no serviço militar daqui {} anos!'.format(alistamento))
elif idade == 18:
    print('Você deve se alistar no serviço militar neste ano!')
    print('Lembre-se, você tem até o dia 29 de junho para se alistar!')
else:
    print('De acordo com sua idade, o tempo de alistamento já se passaram {} ano(s)!'.format(alistamento1))