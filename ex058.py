from termcolor import colored
from time import sleep
from random import randint
p = 0
n1 = randint(0, 10)
print(colored('-_' * 30, 'blue'))
print(colored('Tente adivinhar em qual número entre 0 e 5 estou pensando... ', 'blue'))
print(colored('-_' * 30, 'blue'))
while True:
    n = int(input('Qual número que pensei? '))
    print(colored('Processando ...', 'blue'))
    sleep(1)
    p += 1
    if n == n1:
        print(colored('Parabéns! Você acertou o número sorteado! ', 'green'))
        print('Foram necessários {} palpites!'.format(p))
        break
    else:
        print(colored('Você errou! Tente novamente!', 'red'))


