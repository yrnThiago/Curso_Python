soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Considerando apenas os {} números PARES, a soma é igual a {}'.format(cont, soma))


