import moeda

preco = float(input('Digite o preco: R$:'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(preco, 13)}')