from time import sleep
from termcolor import colored
peso = float(input('Qual o seu peso em Kg? '))
altura = float(input('Qual a sua altura em metros? '))
IMC = peso / altura ** 2
print('Calculando o seu IMC...')
sleep(2)
if IMC < 18.5:
    print('IMC = {:.2f} ( \033[1;31mAbaixo do Peso\033[1m) '.format(IMC))
elif IMC < 25:
    print('IMC = {:.2f} ( \033[1;32mPeso Ideal\033[1m ) '.format(IMC))
elif IMC < 30:
    print('IMC = {:.2f} ( \033[1;33mSobrepeso\033[1m ) '.format(IMC))
elif IMC < 40:
    print('IMC = {:.2f} ( \033[1;31mObesidade\033[1m ) '.format(IMC))
else:
    print('IMC = {:.2f} ( \033[1;31mObesidade Mórbida\033[1m ) '.format(IMC))

