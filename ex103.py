def ficha(nome='', gols=''):
    if nome in '':
        print(f'O jogador <desconhecido> ', end='')
    else:
        print(f'O jogador {nome} ', end='')
    if gols in '':
        print('fez 0 gol(s) no campeonato. ')
    else:
        print(f'fez {gols} gol(s) no campeonato. ')



nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
ficha(nome, gols)
