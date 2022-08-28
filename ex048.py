soma = 0
cont = 0
print('os números ímpares divisiveis por 3:')
for n in range(1, 500, 2):
    if n % 3 == 0:
        print(n)
        soma = soma + n
        cont = cont + 1
print('A soma dos {} valores é igual a {}'.format(cont, soma))
