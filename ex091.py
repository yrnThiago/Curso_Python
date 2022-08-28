from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = list()
for j in range(1, 5):
    jogo[f'Jogador{j}'] = randint(1, 6)
print('Valores sorteados: ')
for i, d in jogo.items():
    print(f'  O {i} tirou {d} no dado. ')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores: ')
for i, v in enumerate(ranking):
    print(f'  {i+1}° lugar: {v[0]} com {v[1]}. ')
    sleep(1)