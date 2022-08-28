print('=-' * 20)
print('         LOJA FAXISTINHA')
print('=-' * 20)
total = m = cont = menor = 0
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    m += 1
    if m == 1:
        menor = preço
        n = nome
    else:
        if preço < menor:
            menor = preço
            n = nome
    if preço > 1000:
        cont += 1
        n = nome
    mais = str(input('Deseja continuar? (S/N) ').upper())
    total += preço
    if mais == 'N':
        break
print('------ Analisando ------')
print(f'Total da compra: R${total:.2f} ')
print(f'{cont} produtos acima de R$1000 ')
print(f'O produto mais barato foi {n} que custa R${menor:.2f}')