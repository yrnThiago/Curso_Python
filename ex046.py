import emoji
from time import sleep
f = 0
print('Contagem regressiva para os fogos de artificio: ')
for f in range(10, 0, -1):
    print(f)
    sleep(1)
print(emoji.emojize(':fireworks:' * 10))
print('Feliz Ano Novo!')
