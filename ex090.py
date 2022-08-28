aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno["Média"] < 7.0:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'
print()
print(f'Nome = {aluno["Nome"]}')
print(f'Média = {aluno["Média"]}')
print(f'Situação = {aluno["Situação"]}')
