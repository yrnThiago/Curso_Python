pessoas = dict()
grupo = list()
mulheres = list()
maisidade = list()
soma = media = 0
while True:
    pessoas['Nome'] = str(input('Nome: '))
    sexo = str(input(('Sexo: (M/F) '))).upper()
    pessoas['Sexo'] = sexo
    idade = int(input('Idade: '))
    pessoas['Idade'] = idade
    soma += pessoas['Idade']
    if 'F' in sexo:
        mulheres.append(pessoas["Nome"])
    resp = str(input('Deseja continuar? (S/N) ')).upper()
    grupo.append(pessoas.copy())
    media = soma / len(grupo)
    if pessoas["Idade"] > media:
        maisidade.append(grupo.copy())
        pessoas.clear()
    pessoas.clear()
    if 'N' in resp:
        break
print('--' * 20)
print(f'- {len(grupo)} pessoas foram cadastradas. ')
print(f'- A média de idade é igual a {media} anos. ')
print(f'- As mulheres cadastradas foram : ', end='')
for m in mulheres:
    print(f'{m}', end=' ')
print()
print('- Lista das pessoas que estão acima da média: ')
for mais in grupo:
    if mais['Idade'] >= media:
        print('   ', end='')
        for k, v in mais.items():
            print(f'{k} = {v}; ', end='')
        print()
print('--' * 20)
print('Finalizando..')
