preço = float(input('Qual o valor do produto? R$'))
dinheiro = preço - preço / 100 * 10
cartão = preço - preço / 100 * 5
cartão2x = preço / 2
juros = preço / 100 * 20
pagamento = input('''Qual o metódo de pagamento?
[ 1 ] à vista no dinheiro/cheque (10% de desconto) 
[ 2 ] à vista no cartão (5% de desconto)
[ 3 ] em até 2x no cartão (preço normal) 
[ 4 ] 3x ou mais no cartão (20% de juros) ''')
if pagamento == '1':
    print('Preço normal do produto: R${:.2f}, com o metódo de pagamento escolhido: "à vista no dinheiro/cheque". O valor do produto com desconto: R${:.2f} '.format(preço, dinheiro))
elif pagamento == '2':
    print('Preço normal do produto: R${:.2f}, com o metódo de pagamento escolhido: "à vista no cartão". O valor do produto com desconto: R${:.2f} '.format(preço, cartão))
elif pagamento == '3':
    print('Preço normal do produto: R${:.2f}, com o metódo de pagamento escolhido: "2x no cartão". 2x de R${:.2f}'.format(preço, cartão2x))
elif pagamento == '4':
    print('Preço normal do produto: R${:.2f}, com o metódo de pagamento escolhido: "3x ou mais no cartão". com 20% de juros.'.format(preço))
    parcelas = int(input("Em quantas parcelas deseja pagar? "))
    cartão3x = preço / parcelas
    print('{}x de R${:.2f}. Preço total do produto: R${:.2f}'.format(parcelas, cartão3x + (juros / 3), preço + juros))
