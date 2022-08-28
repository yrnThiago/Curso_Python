from random import randint  # Para o programa escolher um número aleatório
from time import sleep      # Tempo de espera até o próximo comando
from termcolor import colored     # Adicionar cores no texto
n1 = randint(0, 5)
print(colored('-_' * 30, 'blue'))
print(colored('Tente adivinhar em qual número entre 0 e 5 estou pensando... ', 'blue'))
print(colored('-_' * 30, 'blue'))
n = int(input('Qual número que pensei? '))
print(colored('Processando ...', 'blue'))
sleep(3)
if n == n1:
    print(colored('Parabéns! Você acertou o número sorteado! ', 'green'))
else:
    print(colored('Você perdeu! Pensei no número {} e não no {}! ', 'red').format(n1, n))
    print(colored('Humanos... pff ', 'blue'))


