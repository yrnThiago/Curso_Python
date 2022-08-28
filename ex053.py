f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
inverso =''
for letra in range(len(j) -1, -1, -1):
    inverso += j[letra]
print('Você digitou a palavra {} e o inverso é {}'.format(j, inverso))
if inverso == j:
    print('Essa frase é UM PALÍNDROMO')
else:
    print('Essa frase NÃO é PALÍNDROMO')

