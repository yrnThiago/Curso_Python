n = int(input('Digite um número (999 para PARAR): '))
cont = 0
m = 0
while n != 999:
    cont += 1
    m += n
    n = int(input('Digite um número (999 para PARAR): '))
print('Você digitou {} números e a soma entre eles foi {} . '.format(cont, m))