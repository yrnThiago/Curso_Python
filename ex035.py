r1 = float(input('Qual o comprimento da primeira reta: '))
r2 = float(input('Qual o comprimento da segunda reta: '))
r3 = float(input('Qual o comprimento da terceira reta: '))
a = r2 - r3 < r1 < r2 + r3
b = r1 - r3 < r2 < r1 + r3
c = r1 - r2 < r3 < r1 + r2
print('Analisando as retas: {} cm , {} cm e {} cm ..'.format(r1, r2, r3))
if r2 - r3 < r1 < r2 + r3:
    if r1 - r3 < r2 < r1 + r3:
        if r1 - r2 < r3 < r1 + r2:
            print('É possível fazer um triângulo com essas retas.')
        else:
            print('Não é possível fazer um triângulo com essas retas')
    else:
        print('Não é possível fazer um triângulo com essas retas')
else:
    print('Não é possível fazer um triângulo com essas retas')

