n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
print('Analisando os números: {}, {} e {}'.format(n1, n2, n3))
if n2 > n1:
    maior = n2
    menor = n1
else:
    maior = n1
    menor = n2
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))

