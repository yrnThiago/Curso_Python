somaidade = 0
média = 0
maior = 0
nomevelho = ''
totmulher20 = 0
for n in range(1, 5):
    print('===== {}ª PESSOA ====='.format(n))
    nome = str(input('Nome: '.format(n))).strip()
    idade = int(input('Idade: '.format(n)))
    sexo = str(input('Sexo (M/F): : '.format(n))).strip()
    somaidade += idade
    if n == 1 and sexo in 'm':
        maior = idade
        nomevelho = nome
    if sexo in 'm' and idade > maior:
        maior = idade
        nomevelho = nome
    if sexo in 'f' and idade < 20:
        totmulher20 += 1
média = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(média))
print('O homem mais velho é o {} com {} anos'.format(nomevelho, maior))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
