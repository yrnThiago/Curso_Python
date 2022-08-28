galera = list()
dados = list()
pp = list()
pl = list()
pessoas = pesado = leve = 0
while True:
    nome = str(input('Nome: '))
    dados.append(nome)
    pessoas += 1
    peso = float(input('Peso: '))
    dados.append(peso)
    if pesado == 0 or leve == 0:
        pesado = leve = peso
    else:
        if peso > pesado:
            pesado = peso
        if peso < leve:
            leve = peso
    continuar = str(input('Quer continuar? (S/N) ')).upper()
    galera.append(dados[:])
    dados.clear()
    if 'N' in continuar:
        break
    if continuar not in 'SN':
        print('Opção inválida! Digite S ou N ')
        continuar = str(input('Quer continuar? (S/N) ')).upper()
        if 'N' in continuar:
            break
print('-=' * 20)
print(f'{pessoas} pessoas foram cadastradas! ')
for p in galera:
    if p[1] == pesado:
        pp.append(p[0])
    else:
        if p[1] == leve:
            pl.append(p[0])
print(f'O maior peso foi de {pesado:.2f}. Peso de ', end='')
for nom in pp:
    print(f'[{nom}]', end=' ')
print()
print(f'O menor peso foi de {leve:.2f}. Peso de ', end='')
for no in pl:
    print(f'[{no}]', end=' ')
print()

