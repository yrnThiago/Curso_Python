from datetime import date
trabalho = dict()
trabalho['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
a = date.today().year
trabalho['Idade'] = a - nascimento
trabalho['CTPS'] = int(input('Carteira de Trabalho (0 = Não Possui) '))
if trabalho["CTPS"] != 0:
    trabalho['Ano de Contratação'] = int(input('Ano de contratação: '))
    trabalho['Salário'] = float(input('Salário: R$'))
    trabalho['Aposentadoria'] = trabalho["Ano de Contratação"] + 35 - nascimento
    print()
for t, i in trabalho.items():
    print(f'{t} tem o valor {i}')
