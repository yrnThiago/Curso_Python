from time import sleep
r1 = float(input('Qual o comprimento da primeira reta: '))
r2 = float(input('Qual o comprimento da segunda reta: '))
r3 = float(input('Qual o comprimento da terceira reta: '))
a = r1 == r2 == r3
b = r1 == r2 or r2 == r3 or r3 == r1
print('Analisando as retas: {} cm , {} cm e {} cm...'.format(r1, r2, r3))
sleep(3)
if r2 - r3 < r1 < r2 + r3:
    print('É possível fazer um triângulo com essas retas.')
elif r1 - r3 < r2 < r1 + r3:
    print('É possível fazer um triângulo com essas retas.')
elif r1 - r2 < r3 < r1 + r2:
    print('É possível fazer um triângulo com essas retas.')
else:
    print('Não é possível fazer um triângulo com essas retas')
print('Analisando o triângulo...')
sleep(3)
if a:
    print('O triângulo é EQUILÁTERO!')
elif b:
    print('O triângulo é ISÓSCELES!')
else:
    print('O triângulo é ESCALENO!')

