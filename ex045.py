from random import choice
from time import sleep
print('\033[1;36m=>' * 20)
print('         VAMOS JOGAR JOKENPO: ')
print('<=' * 20)
p = 'Pedra'
pp = 'Papel'
t = 'Tesoura'
jokenpo = p, pp, t
pc = choice(jokenpo)
jogador = int(input('''\033[1;mEscolha: 
[1] Pedra
[2] Papel
[3] Tesoura '''))
if jogador == 1:
    print('Você escolheu: Pedra! ')
    print('O computador escolheu: {}'.format(pc))
elif jogador == 2:
    print('Você escolheu: Papel!')
    print('O computador escolheu: {}'.format(pc))
elif jogador == 3:
    print('Você escolheu: Tesoura! ')
    print('O computador escolheu: {}'.format(pc))
else:
    print('Opcão \033[1;31minválida! \033[mDigite 1 para Pedra, 2 para Papel e 3 para Tesoura..')
sleep(1)
if jogador == 1 and pc == pp:
    print('Você \033[1;31mPERDEU!\033[m Tente novamente. \033[m')
elif jogador == 1 and pc == t:
    print("\033[1;32mParabéns!\033[m Você \033[1;32mGANHOU\033[m do computador! ")
elif jogador == 1 and pc == p:
    print('\033[1;33mEMPATE! \033[mTente novamente! ')
elif jogador == 2 and pc == p:
    print('\033[1;32mParabéns!\033[m Você \033[1;32mGANHOU\033[m do computador!')
elif jogador == 2 and pc == pp:
    print('\033[1;33mEMPATE! \033[mTente novamente. ')
elif jogador == 2 and pc == t:
    print('Você \033[1;31mPERDEU!\033[m Tente novamente. ')
elif jogador == 3 and pc == p:
    print('Você \033[1;31mPERDEU!\033[m Tente novamente. ')
elif jogador == 3 and pc == pp:
    print('\033[1;32mParabéns!\033[m Você \033[1;32mGANHOU\033[m do computador! ')
elif jogador == 3 and pc == t:
    print('\033[1;33mEMPATE!\033[m Tente novamente. ')

