res = 'sS'
m = cont = média = maior = menor = 0
while res in 'sS':
    n = int(input('Digite um número: '))
    m += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    res = str(input('Quer continuar? (S/N) ')).upper().strip()[0]
média = m / cont
print('Você digitou {} números e a média foi {} '.format(cont, média))
print('O maior valor foi {} e o menor foi {} '.format(maior, menor))