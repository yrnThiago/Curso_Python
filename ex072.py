ne = ('zero', 'um', 'dois', 'três', 'quarto', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n > 20:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
if n < 20:
    n
print(f'Você digitou o número {ne[n]}.')
