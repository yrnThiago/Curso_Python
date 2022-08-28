jogador = dict()
partidas = list()
time = list()
total = 0
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for p in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? (S/N) ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if 'N' in resp:
        break
print('--' * 20)
print('Cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()
while True:
    cont = int(input('Mostrar dados de qual jogador? (999 para SAIR do programa) '))
    if cont == 999:
        print('Finalizando o programa..')
        break
    if cont >= len(time):
        print(f'ERRO! Não existe jogador com código {cont}')
        print('--' * 20)
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[cont]["Nome"]} ---')
        for i, g in enumerate(time[cont]["Gols"]):
            print(f' ->Na partida {i+1}, fez {g} gols.')