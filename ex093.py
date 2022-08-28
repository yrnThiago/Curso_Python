jogador = dict()
gol = list()
stats = list()
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
total = 0
for p in range(partidas):
    gols = int(input(f'Quantos gols na partida {p}? '))
    gol.append(gols)
    jogador['Gols'] = gol.copy()
    stats.append(p)
for g in gol:
    total += g
    jogador['Total'] = total
print('=-' * 20)
for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}. ')
print('=-' * 20)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for pp in stats:
    print(f'  ->Na partida {pp}, fez {jogador["Gols"][pp]} gols.')
print(f'Total de {jogador["Total"]} gols. ')